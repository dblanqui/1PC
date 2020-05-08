#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 17:53:47 2020

@author: didier
"""

# -*- coding: utf-8 -*-
from nbautoeval import ExerciseFunction, Args
from nbautoeval import CallRenderer, PPrintRenderer

def composantes_a(xA,yA,xB,yB):
    ax=xB-xA
    ay=yB-yA
    return(ax,ay)


def soustraction_a_b(ax,ay,bx,by):
	cx=ax-bx
	cy=ay-by
	return(cx,cy)

inputs_composantes_a = [
    Args(15,10,20,15),Args(12,5,22,10),Args(5,5,10,10),Args(5,5,5,10),Args(15,10,23,10),Args(15,15,10,12),Args(20,10,15,15)
]

inputs_soustraction_a_b = [
    Args(15,10,20,15),Args(12,5,22,10),Args(5,5,10,10),Args(5,5,5,10),Args(15,10,23,10),Args(15,15,10,12),Args(20,10,15,15)
]


exo_composantes_a = ExerciseFunction(
    composantes_a,
    inputs_composantes_a,
    # show function name in leftmost column
    call_renderer=CallRenderer(show_function=True),
    # use pprint to format results
    result_renderer=PPrintRenderer(width=20),
    font_size="90%",
    header_font_size="120%",
)

exo_soustraction_a_b = ExerciseFunction(
    soustraction_a_b,
    inputs_soustraction_a_b,
    # show function name in leftmost column
    call_renderer=CallRenderer(show_function=True),
    # use pprint to format results
    result_renderer=PPrintRenderer(width=20),
    font_size="90%",
    header_font_size="120%",
)