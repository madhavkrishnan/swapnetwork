`swapnetwork` is a python library to convery `stim` circuits to a
linear-nearest-neighbour (lnn) architecture using `qiskit` synthesis protocols.

# Installation
`swapnetwork` can be installed like any python package from the pyproject.toml
file. For example, using the `pdm` package manager, in the root dir run
```
pdm install .
```

# Usage
`stim` circuits can be made lnn using the `lnn_circuit` function as
```
from swapnetwork.lnn import lnn_circuit

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

lnn_stim_circuit = lnn_circuit(stim_circuit)
print(lnn_stim_circuit)
```

```
H 2
TICK
CX 2 1
TICK
CX 2 3
TICK
SWAP 1 2
TICK
CX 0 1 2 3
TICK
SWAP 2 1
TICK
CX 0 1
TICK
```
