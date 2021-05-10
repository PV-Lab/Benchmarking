# Benchmarking
Benchmarking 

Project Name: Benchmarking the Performance of Bayesian Optimization across Multiple Experimental Materials Science Domains

Corresponding author: Harry Qiaohao Liang (hqliang@mit.edu)

Abstract: 
In the field of machine learning (ML) for materials optimization, active learning algorithms, such as Bayesian Optimization (BO), have enjoyed increased popularity in guiding autonomous high-throughput experimentation systems. However, very few studies have evaluated the efficiency of BO as a general optimization algorithm across a broad range of experimental materials science domains. In this work, we benchmark the performance of BO algorithms with a collection of surrogate model and acquisition function pairs across five diverse experimental materials systems, namely carbon nanotube polymer blends, silver nanoparticles, lead-halide perovskites, as well as additively manufactured polymer structures and shapes. By defining acceleration and enhancement performance metrics for general materials optimization objectives, we find that for surrogate model selection, a Gaussian Process (GP) equipped with anisotropic kernels such as automatic relevance detection (ARD) and Random Forests (RF) have comparable performance and both outclass a GP without ARD. We discuss the implicit distributional assumptions of RF and GP, and the benefits of using GP with anisotropic kernels in detail. We provide practical insights for experimentalists on surrogate model selection of BO during materials optimization campaigns.

GitHub Repo: https://github.com/PV-Lab/Benchmarking

Collaborators: Aldair Gongora, Danny Zekun Ren, Armi Tiihonen, etc.

Status: Paper under peer review.

Explanation of code within GitHub Repo:

After going into each dataset's folder

[1] Dataset name + STANDARD.ipynb

Ensemble Bayesian Optimization runs for each of the datasets to generate benchmarking results.

[2] Dataset name + STANDARD + VIS.ipynb

Result data visualization for each of the datasets to generate figures of metrics such as All, Enhancement Factor, and Acceleration Factor.

[3] Barplot.ipynb

Comparison of BO algorithms' benchmarking results across datasets

