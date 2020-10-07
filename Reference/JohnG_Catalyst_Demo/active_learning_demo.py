#!/usr/bin/env python
# coding: utf-8

# This script first runs a demonstration of active learning and then calculates and plots the acceleration of
# AL by an RF to random selection the second part then shows how different factors in the
# aquisition function influence this acceleration


import pandas as pd
import numpy as np
import pickle
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestRegressor
import matplotlib as mpl
from tqdm import tqdm

from joblib import Parallel, delayed

#load the data containining the composition and performance of a couple of thousand of OER catalysts
#see the paper and related publications for the description of what this is
#in brief: We wat to find materials with a low FOM
data = pickle.load(open(r'tri_data_share.pck','rb'))

#select one of the plates
plates = ['3496']

#inits is the number of random initializations
inits = 50
#nstep_glob is the nuber of active learning steps
nsteps_glob = 300


#for active learning we need a aquisition function. The one we use here simply adds the uncertianty provided
#by the ML algorithm and adds the prediction values to it. Both are weighted with factors that for the sake of this
#demonstration we set both to 1
def acquisition_function(entry_ids, predictions, uncertainties, std_dev_multiplier=1,prediction_multiplier=1):
    acquisition_score = predictions*prediction_multiplier + uncertainties*std_dev_multiplier
    bests = np.where(acquisition_score == np.max(acquisition_score))[0]
    return entry_ids[np.random.choice(bests)]

#There are many runs to do which is why we define a function that performs one active learning run
def al_run(embeddings,metric_array,indexes,best_50,top_perc,nsteps=300,sm=1,pm=1):
    #this runs an active learning initialization to nsteps and return the results
    #embeddings is the data that describes a material i.e. the composition
    #metric_array is the 1D array that contains the FOM to be maximised
    #indexes are the indexes of the materials i.e. 0..n
    #best_50 are the indices of the best 50 materials
    #top_perc are the indices of the top percentile
    #nsteps is the number of active learning steps
    #sm is the multiplier of the uncertianty for the aquisition function
    #pm is the multiplier of the prediction values for the aquisition function

    # we need to save everything on the step level as we want to also estimate model performance at every step later
    idict = {i:[] for i in range(nsteps)}
    #we randomly initialize with one sample
    train_inds = np.random.choice(indexes,1,replace=False)
    #and set all other samples as test
    test_inds = [i for i in indexes if not i in train_inds]
    for i in range(nsteps):
        #we set the estimators and hyperparameters of the regression model here such that other can plug in their
        #model later with minimal changes
        n_estimators = 50
        model = RandomForestRegressor(n_estimators=n_estimators)
        model = model.fit(embeddings[train_inds,:], metric_array[train_inds])
        predictions = model.predict(embeddings[test_inds,:])
        tree_predictions = np.zeros((len(test_inds), n_estimators))
        for j in range(n_estimators):
            tree_predictions[:,j] = model.estimators_[j].predict(embeddings[test_inds,:])
        uncertainties = np.std(tree_predictions, axis=1)
        #we call the aquisition function to return a index to be appended onto the train data
        acquired_entry_id = acquisition_function(indexes[test_inds], predictions,
                                                 uncertainties, std_dev_multiplier=sm,prediction_multiplier=pm)
        train_inds = np.append(train_inds, acquired_entry_id)
        test_inds = np.delete(test_inds, np.where(test_inds==acquired_entry_id))
        idict[i] = {'train_list':train_inds,'test_list':test_inds,'top_50':best_50,
                    'top_perc':top_perc,'pred_test':model.predict(embeddings),'val_test':metric_array}
    return idict

#though we have an equation for the expectiation of "random" active learning we do need to perform it
#to estimate the acceleration and deceleration of active learning for model improvement
def rand_run(embeddings,metric_array,indexes,best_50,top_perc,nsteps=300):
    #this runs an active learning initialization to nsteps and return the results
    idict = {i:[] for i in range(nsteps)}
    train_inds = np.random.choice(indexes,1,replace=False)
    test_inds = [i for i in indexes if not i in train_inds]
    for i in range(nsteps):
        n_estimators = 50
        model = RandomForestRegressor(n_estimators=n_estimators)
        model = model.fit(embeddings[train_inds,:], metric_array[train_inds])
        predictions = model.predict(embeddings[test_inds,:])
        #essentially this function is the same as the above except for that the "aquisition" function
        #randomly chooses the next sample to be added
        acquired_entry_id = acquired_entry_id = np.random.choice(indexes[test_inds],1)[0]
        train_inds = np.append(train_inds, acquired_entry_id)
        test_inds = np.delete(test_inds, np.where(test_inds==acquired_entry_id))
        idict[i] = {'train_list':train_inds,'test_list':test_inds,'top_50':best_50,'top_perc':top_perc,
                    'pred_test':model.predict(embeddings),'val_test':metric_array}
    return idict


modes = ['equal']
active_results = {k:{p:{i:[] for i in range(inits)} for p in plates} for k in modes}
random_results = {p:{i:[] for i in range(inits)} for p in plates}


for mi,pair in enumerate([[1,1]]):
    mode = modes[mi]
    pm = pair[0]
    sm = pair[1]

    #one plate takes ca. 10 minutes to run on a powerful PC
    for plate in plates:
        print('Starting AL on plate {}'.format(plate))
        embeddings = np.array(data[plate]['comp'])
        metric_array = -np.array(data[plate]['fom']) #take the negative because we actually seek a small FOM
        indexes = np.array([i for i in range(len(metric_array))])

        best_50 = np.argsort(metric_array)[-50:]
        top_perc = np.where(metric_array>np.percentile(metric_array,99))[0]

        d = Parallel(n_jobs=5)(delayed(al_run)(embeddings,metric_array,indexes,best_50,top_perc,nsteps_glob,sm,pm) for start in tqdm(range(inits)))
        pickle.dump(d,open(r'active_learning_benchmark_{}_{}_sm{}_pm{}.pck'.format(mode,plate,sm,pm),'wb'))


for plate in plates:
    print('Starting random on plate {}'.format(plate))
    embeddings = np.array(data[plate]['comp'])
    metric_array = -np.array(data[plate]['fom']) #take the negative because we need to have min overpotential
    indexes = np.array([i for i in range(len(metric_array))])

    best_50 = np.argsort(metric_array)[-50:]
    top_perc = np.where(metric_array>np.percentile(metric_array,99))[0]

    d = Parallel(n_jobs=-1)(delayed(rand_run)(embeddings,metric_array,indexes,best_50,top_perc,nsteps_glob) for start in tqdm(range(inits)))
    pickle.dump(d,open(r'active_learning_benchmark_random_baseline_{}.pck'.format(plate),'wb'))
