from qiskit_ibm_runtime import QiskitRuntimeService

QiskitRuntimeService.save_account(
    channel="ibm_quantum_platform",   # fixed for free/open IBM Quantum accounts
    token="API-Key",
    overwrite=True
)

