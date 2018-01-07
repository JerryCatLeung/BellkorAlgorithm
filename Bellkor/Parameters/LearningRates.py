#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Bellkor.Parameters.LearningRates
"""
from Bellkor.Base.Generic import Generic


class LearningRates(Generic):
    """ Learning Rates
    """
    b_u = 5e-3
    alpha_u = 1e-4
    b_i = 2e-2
    c_u = 5e-3
    b_ut = 2e-2
    c_ut = 2e-2
    b_ibin = 1e-4
    p = 5e-3
    q = 5e-3
    alpha_p = 1e-4

    def __repr__(self):
        return "< Default Learning Rates >"
