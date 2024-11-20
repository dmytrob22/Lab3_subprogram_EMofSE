from SequenceTest import SequenceTester  # Import the SequenceTester class which handles sequence generation and mode calculation


class Application:
    # The Application class is the main controller for generating sequences, calculating their modes,
    # and displaying the results. The value 'n' is passed to this class to determine the size of sequences.

    def __init__(self, n):
        """
        Initializes the Application with a given parameter 'n'.
        'n' is the base number for generating sequences.
        """
        self.n = n  # Assign 'n' which will be used to define the range and size of sequences

    def run(self):
        """
        Runs the application, generating sequences, calculating their modes, and displaying the results.
        This method creates an instance of the SequenceTester class, uses it to generate sequences,
        calculate their modes, and then display the results.
        """
        # Create an instance of the SequenceTester class with the provided 'n'
        tester = SequenceTester(self.n)

        # Generate a list of sequences using the SequenceTester instance
        tester.generate_sequences()

        # Calculate the mode of each generated sequence
        tester.calculate_modes()

        # Display the sequences along with their calculated modes
        tester.display_results()
