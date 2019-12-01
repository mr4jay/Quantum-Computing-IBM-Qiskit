from qiskit import QuantumRegister,QuantumCircuit,execute,Aer
from qiskit import IBMQ
IBMQ.load_account()
S_simulator=Aer.backends(name='statevector_simulator')[0]
M_simulator=Aer.backends(name='qasm_simulator')[0]

q=QuantumRegister(1)
hello_qubit=QuantumCircuit(q)

hello_qubit.x(q[0])


job=execute(hello_qubit,S_simulator)
result=job.result()
result.get_statevector()

