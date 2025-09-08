"""
Code to transpile stim circuits for LNN architectures.
"""
import stim
from qiskit import transpile
from qiskit.transpiler import CouplingMap
import qiskit.qasm2
from stimcirq import stim_circuit_to_cirq_circuit, cirq_circuit_to_stim_circuit
from cirq import num_qubits
from cirq.contrib.qasm_import import circuit_from_qasm as qasm2cirq

def lnn_circuit(stim_circuit: 'stim.Circuit') -> 'stim.Circuit':
    """
    Converts a given stim circuit to linear-nearest-neighbour stim circuit,
    i.e., a circuit with gates acting only adjacent qubits.
    
    This function uses qiskit's transpilation which seems? to use

    "References:
        1. Kutin, S., Moulton, D. P., Smithline, L.,
           *Computation at a distance*, Chicago J. Theor. Comput. Sci., vol. 
           2007, (2007),`arXiv:quant-ph/0701194 
           <https://arxiv.org/abs/quant-ph/0701194>`_"
    
    This method promises:
    Depth  <= 5n
    Gate count = O(n^2)
    
    code ref: 
    https://quantum.cloud.ibm.com/docs/en/api/qiskit/synthesis
    """
    # stim -> cirq -> qiskit
    cirq_circuit = stim_circuit_to_cirq_circuit(stim_circuit)
    qubits = num_qubits(cirq_circuit)
    qasm_str = cirq_circuit.to_qasm(version="2.0")
    qiskit_circuit = qiskit.qasm2.loads(qasm_str)

    # Transpile to lnn
    lnn_map = CouplingMap.from_line(qubits)
    lnn_qc = transpile(qiskit_circuit, coupling_map=lnn_map)

    # qasm -> cirq -> stim
    qasm_str = qiskit.qasm2.dumps(lnn_qc)
    cirq_circuit = qasm2cirq(qasm_str)
    stim_circuit = cirq_circuit_to_stim_circuit(cirq_circuit)
    
    return stim_circuit

def swap_network(permutation) -> "stim.Circuit":
    """
    Returns a nearest neighbour swap network
    """
    pass
