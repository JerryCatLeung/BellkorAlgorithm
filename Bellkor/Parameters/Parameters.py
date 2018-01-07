#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Bellkor.Parameters.Parameters
"""
import numpy as np


class Parameters:
    """ Model Parameter Storage
    """
    alpha_p = dict()
    alpha_u = dict()
    b_i = dict()
    b_ibin = np.array([])
    b_u = dict()
    b_ut = np.array([])
    c_u = dict()
    c_ut = np.array([])
    p = dict()
    q = dict()

    def __repr__(self):
        return "< Model Parameter Storage >"

    def size(self):
        return len(self.c_u)
