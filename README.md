# Benchmarking
Benchmarking 

Project Name: (Tentative) Benchmarking

Project Leader: Harry Qiaohao Liang (hqliang@mit.edu)

Abstract: 
In the field of machine learning (ML) for materials optimization, active learning algorithms like Bayesian Optimization (BO) have been widely used to guide high- throughput autonomous experiments. However, very few studies have evaluated the efficiency of BO as a general optimization algorithm for a wide range of material systems. In this work, we apply a benchmarking framework to evaluate the performance of BO across five diverse experimental materials science domains. With acceleration and enhancement metrics defined for specific research objectives, we show that random forests (RF) paired with lower confidence bound (LCB) outclass other combinations of surrogate models and acquisition functions commonly used in BO. Our analysis of RF’s performance and practicality as surrogate model has also yielded many useful insights on how materials scientists could select the most suitable BO algorithms to improve their optimization campaigns. 

GitHub Repo: https://github.com/PV-Lab/Benchmarking

Collaborators:

Aldair Gongora, Danny Zekun Ren, Armi Tiihonen, Liu Zhe, etc.

Location of other data:

[1] \Buonassisi-Group\AMD Team\Benchmarking\04_Data

Sponsors: TOTAL

Explanation of code within GitHub Repo:

After going into each dataset's folder

[1] Dataset name + STANDARD.ipynb

Ensemble Bayesian Optimization runs for each of the datasets to generate benchmarking results.

[2] Dataset name + STANDARD + VIS.ipynb

Result data visualization for each of the datasets to generate figures of metrics such as All, Enhancement Factor, and Acceleration Factor.

[3] Barplot.ipynb

Comparison of BO algorithms' benchmarking results across datasets

