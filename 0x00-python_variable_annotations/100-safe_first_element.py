#!/usr/bin/env python3
"""
100-safe_first_element.py
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    a type-annotated function safe_first_element that takes a Sequence[Any]
    as argument and returns the first element of the Sequence if it is not
    empty, and None otherwise.
    """
    if lst:
        return lst[0]
    else:
        return None
