#!/usr/bin/env python3

from typing import Tuple

def zoom_array(lst: Tuple[int], factor: int =2) -> Tuple[int]:
    zoomed_in = tuple(item for item in lst for _ in range(factor))
    return zoomed_in

array = (12, 72, 91)  # Use a tuple instead of a list for the array

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)  # Use an integer as the factor