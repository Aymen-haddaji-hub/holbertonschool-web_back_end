#!/usr/bin/env python3
"""
9-element_length.py"""
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    a type-annotated function element_length that takes an
    Iterable[Sequence] as argument and returns a List[Tuple[Sequence, int]].
    The first element of each tuple is the Sequence.
    The second element is the length of the Sequence
    and should be annotated as an int.
    """
    return [(i, len(i)) for i in lst]
