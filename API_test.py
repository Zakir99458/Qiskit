from qiskit_ibm_runtime import QiskitRuntimeService

QiskitRuntimeService.save_account(
    channel="ibm_quantum_platform",   # fixed for free/open IBM Quantum accounts
    token="ApiKey-98158ff7-c9ca-4be0-90a9-1006b0a0edad"
)
