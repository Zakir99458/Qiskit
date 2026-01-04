from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
# Checking the output from Quantum Circuit for Not Gate
qc1 = QuantumCircuit(2)
qc1.x(0)
qc1.cx(0,1)
state_not = Statevector.from_instruction(qc1)
print(state_not)
# Checking the output from Quantum Circuit for Hadamard (H) gate
qc2 = QuantumCircuit(2)
qc2.h(0)
qc2.cx(0,1)
state_h = Statevector.from_instruction(qc2)
print(state_h)
