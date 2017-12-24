#!/usr/local/miniconda2/bin/python
# _*_ coding: utf-8 _*_

"""
@author: MarkLiu
@time  : 17-6-26 下午3:14
"""
import os
import sys

module_path = os.path.abspath(os.path.join('..'))
sys.path.append(module_path)

import time


class Configure(object):

    train_data_path = '../input/train/audio'
    test_data_path = '../input/test/audio'

    submission_path = '../output/submission_{}.csv'.format(time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time())))