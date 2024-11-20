from collections import Counter


class Mode:
    # The Mode class calculates the mode(s) of a dataset.
    # The mode is the value(s) that appear most frequently in a dataset.
    # If multiple values appear with the same maximum frequency, all those values are considered modes.

    @staticmethod
    def calculate(data):
        counts = Counter(data)

        max_count = max(counts.values())

        modes = [value for value, count in counts.items() if count == max_count]

        return modes[0] if len(modes) == 1 else modes
