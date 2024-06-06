#!/usr/bin/env python3
# 6-sum_mixed_list.py
""" Type annotated fx """

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    ''' Return sum of elements of mxd_list. '''
    return sum(mxd_lst)
