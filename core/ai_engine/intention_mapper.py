"""Map user intention (text) to frequency profiles.
Placeholder using simple keyword mapping; replace with ML model.
"""

MAPPING = {
    'healing': '528',
    'love': '639',
}


def map_intention(text):
    for k, v in MAPPING.items():
        if k in text.lower():
            return v
    return '528'
