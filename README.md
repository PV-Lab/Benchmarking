# Benchmarking
Benchmarking 

Project Name: Benchmarking the Performance of Bayesian Optimization across Multiple Experimental Materials Science Domains

## Authors
||                    |
| ------------- | ------------------------------ |
| **AUTHORS**      | Harry Qiaohao Liang     | 
| **VERSION**      | 1.0 / April, 2021     | 
| **EMAILS**      | hqliang@mit.edu | 
||                    |


Abstract: 
In the field of machine learning (ML) for materials optimization, active learning algorithms, such as Bayesian Optimization (BO), have enjoyed increased popularity in guiding autonomous high-throughput experimentation systems. However, very few studies have evaluated the efficiency of BO as a general optimization algorithm across a broad range of experimental materials science domains. In this work, we benchmark the performance of BO algorithms with a collection of surrogate model and acquisition function pairs across five diverse experimental materials systems, namely carbon nanotube polymer blends, silver nanoparticles, lead-halide perovskites, as well as additively manufactured polymer structures and shapes. By defining acceleration and enhancement performance metrics for general materials optimization objectives, we find that for surrogate model selection, a Gaussian Process (GP) equipped with anisotropic kernels such as automatic relevance detection (ARD) and Random Forests (RF) have comparable performance and both outclass a GP without ARD. We discuss the implicit distributional assumptions of RF and GP, and the benefits of using GP with anisotropic kernels in detail. We provide practical insights for experimentalists on surrogate model selection of BO during materials optimization campaigns.

GitHub Repo: https://github.com/PV-Lab/Benchmarking

Collaborators: Aldair Gongora, Danny Zekun Ren, Armi Tiihonen, etc.

Status: Paper under peer review.

Molecule data in this repository is provided by Sarah J. Cox-Vazquez, Cheng Zhou, Nathan C. Incandela, Jakkarin Limwonguyt, Alex S. Moreland, and Guillermo C. Bazan.



Try the desired parts of the project:
- Main_downselection.py: Generates datafiles for other codes. Repeats molecular descriptor downselection for the data and trains RF models at each stage of downselection.
- Main_training_models.py: Trains RF, XGB, and GP models with downselected molecular fingerprints and reference fingerprints.
- SHAP_for_RF_analysis.ipynb: Investigate the final RF model trained with Opt. fingerprint using SHAP analysis.
- Main_train_test_chemprop_models_stratified_split.sh: Train and test DMPNN and ffNN models. Running this code may take an hour or so, therefore it is better to run on a server. Alternatively, the fully trained model is available by request from the authors (not included into this repository due to its large size).
- Main_plot_chemprop_models_and_violins.py: Plot neural network model results and all the violin plots. Works only after Main_train_test_chemprop_models_stratigfied_split.sh has been run.
- RFE_RF_run.sh: Run RFE for Cor. descriptors. Running this code may take an hour or so, therefore it is better to run on a server.
- HO_RF_init_var_cor.sh: Hyperparameter optimization for RF. Running this code may take an hour or so, therefore it is better to run on a server.
- Results: All the resulting figures created when running the codes. 



## Attribution
This work is under BSD-2-Clause License. Please, acknowledge use of this work with the appropiate citation to the repository and research article.

## Citation

    @Misc{benchmarking2021,
      author =   {Liang et al.},
      title =    {Benchmarking the Performance of Bayesian Optimization across Multiple Experimental Materials Science Domains},
      howpublished = {\url{https://github.com/PV-Lab/Benchmarking}},
      year = {2021}
    }
Article citation coming soon.

