#!/usr/bin/env python3

from typing import Optional

def safe_first_element(lst) -> Optional:
    """
    Augment the following code with the 
    correct duck-typed annotations:
    """
    if lst:
        return lst[0]
    else:
        return None
