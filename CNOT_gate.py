from qiskit import ClassicalRegister,QuantumRegister,QuantumCircuit,Aer
from qiskit.tools.visualization import circuit_drawer
from qiskit import IBMQ
IBMQ.load_account()
S_simulator=Aer.backends(name='statevector_simulator')[0]
M_simulator=Aer.backends(name='qasm_simulator')[0]

q=QuantumRegister(2,name='q')
c=ClassicalRegister(2,name='c')
qc=QuantumCircuit(q,c,name='qc')

qc.iden(q[0])
qc.iden(q[1])
qc.cx(q[0],q[1])

print(circuit_drawer(qc))