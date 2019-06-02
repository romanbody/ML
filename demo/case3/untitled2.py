#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 16:27:25 2019

@author: romanbody
"""

from keras import models
from keras import layers

from keras.utils import plot_model


network = models.Sequential()

#network.add(layers.Dense(units=16,activation='relu',input_shape(10,)))
network.add(layers.Dense(units=16,activation='relu'))

network.add(layers.Dense(units=16,activation='relu'))

network.add(layers.Dense(units=1,activation='sigmoid'))

network.compile(loss='binary_crossentropy',optimizer='rmsprop',metrics=["accuracy"])

plot_model(network,show_shapes=True)