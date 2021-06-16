## Introduction

Check `FCN.ipynb`, `alexnet.ipynb` and `resnet.ipynb` for the implementation of our experiment.

Folder `ResNet_experiments`: resnet.ipynb contains implementation of resnet. Functionalities in "ResNet_experiments/utils.py" are same as functionalities in "sgd_tail_index_maser/utils.py" but only modified a very tiny bit for convenience. 

Folder `sgd_tail_index-master`: We  used  the  source  code  provided  by  (Simsekli et al., 2019) but modified it to our own requirements. 

Folder `sgd_tail_index-master/PyHessian`: The  code  for computing the Hessian information was taken from (Yao et al.,2020). 

Data: Please download "MNIST" and "CIFAR-10" datasets for running the experiments.


## How to run:

For `alexnet.ipynb` and `FCN.ipynb`, please add a line of code to enter the `sgd_tail_index-master` folder at the begining of the notebook, and then run the notebook.

For example, if one run it locally, one can add the following line at the begining of the notebook:
```python
%cd ./sgd_tail_index-master/
```

This is because we need to invoke `./sgd_tail_index-master/main.py` to train the network in `alexnet.ipynb` and `FCN.ipynb`

For `resnet.ipynb`, one can run  the notebook directly.