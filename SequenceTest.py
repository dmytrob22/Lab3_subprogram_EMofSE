import random
from Mode import Mode


class SequenceTester:
    # The SequenceTester class is responsible for generating multiple sequences, calculating their modes,
    # and displaying the results.

    def __init__(self, n, num_sequences=5):
        # The constructor initializes the sequence tester with the following parameters:
        # - n: The size of each sequence minus 10.
        # - num_sequences: The number of sequences to generate.
        # The default value of num_sequences is set to 5.

        self.n = n  # The size of each sequence minus 10.
        self.num_sequences = num_sequences  # The number of sequences to generate.
        self.value_range = n + 1  # The maximum value in the sequence is n + 1.
        self.sequences = []  # This will hold all the generated sequences.
        self.results = []  # This will hold the mode of each sequence.

    def generate_sequences(self):
        # This method generates `num_sequences` random sequences, each of length `n + 10`.
        for _ in range(self.num_sequences):
            sequence = [random.randint(1, self.value_range) for _ in range(self.n + 10)]
            self.sequences.append(sequence)  # Add the generated sequence to the list of sequences

    def calculate_modes(self):
        # This method calculates the mode of each generated sequence using the Mode class.
        for sequence in self.sequences:
            mode = Mode.calculate(sequence)  # Calculate the mode of the sequence
            self.results.append({"Sequence": sequence, "Mode": mode})  # Store the result with the sequence and its mode

    def display_results(self):
        # This method displays the results: each sequence and its corresponding mode.

        # Print a header with formatted column names for Sequence and Mode.
        print(f"{'Sequence':<50} {'Mode':<10}")
        print("-" * 60)  # Print a separator line

        # Iterate over the results and display each sequence and its mode.
        for result in self.results:
            sequence_str = ', '.join(map(str, result['Sequence']))  # Convert the sequence list to a string
            print(f"{sequence_str:<50} {result['Mode']}")  # Print the sequence and its mode in a formatted manner
            sorted_sequence_str = ', '.join(map(str, sorted(result['Sequence'])))  # Convert the sorted sequence list to a string
            print(f"{sorted_sequence_str:<50}")  # Print the sorted sequence
            print()
