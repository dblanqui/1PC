#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 17:53:47 2020

@author: didier
"""

# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args

def normes_a(xA,yA,xB,yB):
    ax=xB-xA
    ay=yB-yA
    return(ax,ay)

inputs_normes_a = [
    Args(15,10,20,15),Args(12,5,22,10),Args(5,5,10,10),Args(5,5,5,10),Args(15,10,23,10),Args(15,15,10,12),Args(20,10,15,15)
]

exo_normes_a = ExerciseFunction(
    normes_a,
    inputs_normes_a,
    layout='pprint',
    layout_args=(40, 25, 25),
)