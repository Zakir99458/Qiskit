import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

qc1 = QuantumCircuit(1)
qc1.h(0)  # apply H gate : generate superposition

state1 = Statevector.from_instruction(qc1)
print("H on |0>:", state1)

# Applying not before the hadamard gate
qc2 = QuantumCircuit(1)
qc2.x(0) # make the initial state to 1 for hadamard gate
qc2.h(0)
state2 = Statevector.from_instruction(qc2)
print("H on ! change to 1",state2)
