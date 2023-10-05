#!/usr/bin/env python3
from typing import List,Tuple
"""
Annotate the below function’s parameters and 
return values with the appropriate types
"""
def element_length(lst: List[str]) -> List[tuple[str, int]]:
    return[(i, len(i)) for i in lst]
