"""DSP utility functions."""

import math


def hz_to_note(freq):
    return 69 + 12 * math.log2(freq / 440.0)
