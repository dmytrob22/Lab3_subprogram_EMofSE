from collections import Counter  # Import Counter from the collections module to count occurrences of elements


class Mode:
    # The Mode class calculates the mode(s) of a dataset.
    # The mode is the value(s) that appear most frequently in a dataset.
    # If multiple values appear with the same maximum frequency, all those values are considered modes.

    @staticmethod
    def calculate(data):
        """
        This method calculates the mode(s) of a dataset. It returns the mode if there is one,
        or a list of modes if there are multiple values with the same highest frequency.
        """

        # Create a Counter object to count occurrences of each element in the dataset (data)
        counts = Counter(data)

        # Find the maximum count (the highest frequency)
        max_count = max(counts.values())

        # Collect all values that have the maximum count (i.e., the mode or modes)
        modes = [value for value, count in counts.items() if count == max_count]

        # If there is only one mode, return it; otherwise, return a list of modes
        return modes[0] if len(modes) == 1 else modes
