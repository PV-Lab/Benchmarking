# Benchmarking

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

## Attribution
This work is under BSD-2-Clause License. Please, acknowledge use of this work with the appropiate citation to the repository and research article.

## Citation 

    @Misc{benchmarking2021,
      title={Benchmarking the Performance of Bayesian Optimization across Multiple Experimental Materials Science Domains},
      author={Liang et al.},
      howpublished = {\url{https://github.com/PV-Lab/Benchmarking}},
      year = {2021}
    }
    (Article citation coming soon.)

## Datasets
For reuse for code and materials datasets in this repo, please cite both the this study above and the authors for their datasets.

Materials datasets used to benchmark BO performance in this repository is provided by:

(1) Crossed barrel dataset

    @article{gongora2020bayesian,
      title={A Bayesian experimental autonomous researcher for mechanical design},
      author={Gongora, Aldair E and Xu, Bowen and Perry, Wyatt and Okoye, Chika and Riley, Patrick and Reyes, Kristofer G and Morgan, Elise F and Brown, Keith A},
      journal={Science advances},
      volume={6},
      number={15},
      pages={eaaz1708},
      year={2020},
      publisher={American Association for the Advancement of Science}
    }
    
(2) Perovskite
     
     @article{sun2021data,
       title={A data fusion approach to optimize compositional stability of halide perovskites},
       author={Sun, Shijing and Tiihonen, Armi and Oviedo, Felipe and Liu, Zhe and Thapa, Janak and Zhao, Yicheng and Hartono, Noor Titan P and Goyal, Anuj and Heumueller, Thomas and Batali, Clio and others},
       journal={Matter},
       volume={4},
       number={4},
       pages={1305--1322},
       year={2021},
       publisher={Elsevier}
     }
     
(3) AutoAM

     @article{deneault2021toward,
       title={Toward autonomous additive manufacturing: Bayesian optimization on a 3D printer},
       author={Deneault, James R and Chang, Jorge and Myung, Jay and Hooper, Daylond and Armstrong, Andrew and Pitt, Mark and Maruyama, Benji},
       journal={MRS Bulletin},
       pages={1--10},
       year={2021},    
       publisher={Springer}
     }
     
(4) P3HT/CNT

    @article{bash2020machine,
      title={Machine learning and high-throughput robust design of P3HT-CNT composite thin films for high electrical conductivity},
      author={Bash, Daniil and Cai, Yongqiang and Chellappan, Vijila and Wong, Swee Liang and Xu, Yang and Kumar, Pawan and Da Tan, Jin and Abutaha, Anas and Cheng, Jayce and Lim, Yee Fun and others},
      journal={arXiv preprint arXiv:2011.10382},
      year={2020}
    }
    
(5) AgNP

    @article{mekki2021two,
      title={Two-step machine learning enables optimized nanoparticle synthesis},
      author={Mekki-Berrada, Flore and Ren, Zekun and Huang, Tan and Wong, Wai Kuan and Zheng, Fang and Xie, Jiaxun and Tian, Isaac Parker Siyu and Jayavelu, Senthilnath and Mahfoud, Zackaria and Bash, Daniil and others},
      journal={npj Computational Materials},
      volume={7},
      number={1},
      pages={1--10},
      year={2021},
      publisher={Nature Publishing Group}
    }



Try the desired parts of the project:
- Main_downselection.py: Generates datafiles for other codes. Repeats molecular descriptor downselection for the data and trains RF models at each stage of downselection.
- Main_training_models.py: Trains RF, XGB, and GP models with downselected molecular fingerprints and reference fingerprints.
- SHAP_for_RF_analysis.ipynb: Investigate the final RF model trained with Opt. fingerprint using SHAP analysis.
- Main_train_test_chemprop_models_stratified_split.sh: Train and test DMPNN and ffNN models. Running this code may take an hour or so, therefore it is better to run on a server. Alternatively, the fully trained model is available by request from the authors (not included into this repository due to its large size).
- Main_plot_chemprop_models_and_violins.py: Plot neural network model results and all the violin plots. Works only after Main_train_test_chemprop_models_stratigfied_split.sh has been run.
- RFE_RF_run.sh: Run RFE for Cor. descriptors. Running this code may take an hour or so, therefore it is better to run on a server.
- HO_RF_init_var_cor.sh: Hyperparameter optimization for RF. Running this code may take an hour or so, therefore it is better to run on a server.
- Results: All the resulting figures created when running the codes. 





