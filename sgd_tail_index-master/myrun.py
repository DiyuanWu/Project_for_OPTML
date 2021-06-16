import os
import subprocess
import itertools
import time
import torch

import numpy as np
import matplotlib.pyplot as plt

# analysis of Hessian
# !git clone https://github.com/amirgholami/PyHessian.git
import sys
sys.path.append('/content/PyHessian/')



# folder to save
base_path = 'results_FC_scales'

if not os.path.exists(base_path):
    os.makedirs(base_path)

# server setup
# launcher = "srun --nodes=1 --gres=gpu:1 --time=40:00:00 --mem=60G" # THIS IS AN EXAMPLE!!!

# experimental setup
# width = [4, 8, 16, 32, 64, 128, 256, 512, 1024]
# depth = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# seeds = list(range(3))
# dataset = ['mnist', 'cifar10']
# loss = ['NLL','linear_hinge']
# dataset = ['mnist']
# model = ['fc']
w = 4
dep = 2
s = 0
l = 'NLL'
d = 'cifar10'
m = 'alexnet'

iter = 20000
eval_freq = 100 # don't vary it; keep it the same as in the code
close_check_lb = 900
close_check_hb = 2000
close_check_freq = 10
eval_Hessian_freq = 5000
# grid = itertools.product(width, depth, seeds, dataset, loss, model)

processes = []
# for w, dep, s, d, l, m in grid:

save_dir = base_path + '/{}_{:04d}_{:02d}_{}_{}_{}'.format(dep, w, s, d, l, m)
if os.path.exists(save_dir):
    # folder created only at the end when all is done!
    print('folder already exists, quitting')
    # continue

# cmd = launcher + ' '
cmd = 'python main.py '
cmd += '--save_dir {} '.format(save_dir)
if m == 'fc':
  cmd += '--width {} '.format(w)
elif m == 'alexnet':
  cmd += '--scale {} '.format(w)
cmd += '--depth {} '.format(dep)
cmd += '--seed {} '.format(s)
cmd += '--dataset {} '.format(d)
cmd += '--model {} '.format(m)
cmd += '--lr {} '.format('0.1')
cmd += '--lr_schedule '
cmd += '--iterations {} '.format(iter)
cmd += '--eval_freq {} '.format(eval_freq)
cmd += '--close_check_lb {} '.format(close_check_lb)
cmd += '--close_check_hb {} '.format(close_check_hb)
cmd += '--close_check_freq {} '.format(close_check_freq)
cmd += '--eval_Hessian_freq {} '.format(eval_Hessian_freq)
# cmd += '--print_freq {} '.format(1), # dbg
# cmd += '--verbose '

# print(cmd)

f = open(save_dir + '.log', 'w')

print(cmd)
# subprocess.Popen(cmd.split(), stdout=f, stderr=f)#.wait()
   