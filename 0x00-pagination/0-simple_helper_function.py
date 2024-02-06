#!/usr/bin/env python3

""" Getting the index range for pagination"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        This function takes two interger args
    args:
        page: page number
        page_size: the size of one page

    returns:
        A tuple with the starting index and end index
    """

    first_index = (page - 1) * page_size
    last_index = page_size + first_index

    return first_index, last_index
