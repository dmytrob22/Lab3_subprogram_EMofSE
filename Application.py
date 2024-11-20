from SequenceTest import SequenceTester


class Application:
    # The Application class is the main controller for generating sequences, calculating their modes,
    # and displaying the results. The value 'n' is passed to this class to determine the size of sequences.

    def __init__(self, n):
        self.n = n

    def run(self):
        tester = SequenceTester(self.n)

        tester.generate_sequences()

        tester.calculate_modes()

        tester.display_results()
