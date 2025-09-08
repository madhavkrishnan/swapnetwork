import unittest
import stim
from swapnetwork.lnn import lnn_circuit

class LnnTests(unittest.TestCase):
    """
    Test conversion of stim circuit to lnn
    """
    def test_lnn_circuit(self, stim_circuit=None):
        if stim_circuit is None:
            stim_circuit = stim.Circuit(
                '''
                H 0
                CX 0 1
                CX 0 2
                CX 1 2
                CX 3 0
                CX 3 1
                '''
            )
        print("\n")
        print(lnn_circuit(stim_circuit))

if __name__ == "__main__":
    unittest.main()
