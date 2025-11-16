"""Math utilities."""
import math


def clamp(x, a, b):
    return max(a, min(b, x))
