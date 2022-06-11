#!/usr/bin/env python3
"""
101-safely_get_value.py
"""
from typing import Union, Mapping, Any, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    a type-annotated function safely_get_value that takes a Mapping and a key
    as arguments and returns the value associated with the key in the Mapping
    if it exists, and the default value otherwise.
    """
    if key in dct:
        return dct[key]
    else:
        return default
