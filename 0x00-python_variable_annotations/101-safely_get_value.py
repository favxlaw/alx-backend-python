#!/usr/bin/env python3

from typing import TypeVar, Dict, Optional

V = TypeVar('V')

def safely_get_value(dct: Dict[str, V], key: str, default: Optional[V] = None) -> V:
    if key in dct:
        return dct[key]
    else:
        return default
    