from __future__ import print_function

from builtins import input
from random import shuffle
from topologylayer.nn import LevelSetLayer2D, SumBarcodeLengths, PartialSumBarcodeLengths
from six.moves import range
from torch.utils import data
from tqdm import tqdm
import sys
import time
import itertools as it
import glob
import numpy as np
import h5py
import scipy.io as io
import torch
import torch.nn.functional as F
import torch.nn as nn


inputData = './test2.hdf5'

#load the model
nEpoch = 2000
model = torch.load("model-epoch" + str(nEpoch) + ".pt")

#load the dataset
# Import Data
f = h5py.File(inputData, 'r')
im = np.array(f.get('/im'))
im = im.reshape(im.shape + (1,))
imSize = im.size
imShape = im.shape
if isTrain:
    l = np.array(f.get('/l'))
    l = l.reshape(l.shape + (1,))
    nc = im.shape[1]
    tst = im[:, :(nc // 4), :]
    tstL = l[:, :(nc // 4), :]
    trn = im[:, (nc // 2):, :]
    trnL = l[:, (nc // 2):, :]
    tst = np.pad(tst, padSize, 'symmetric')
    trn = np.pad(trn, padSize, 'symmetric')
if isForward:
    im = np.pad(im, padSize, 'symmetric')
    V = np.zeros(imShape, dtype=np.float32)
print("Data loaded.")


python DeepVess.py ../../test2.hdf5 