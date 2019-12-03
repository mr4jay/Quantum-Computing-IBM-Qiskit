from qiskit import ClassicalRegister,QuantumRegister,QuantumCircuit,Aer
from qiskit import IBMQ
IBMQ.load_account()
S_simulator=Aer.backends(name='statevector_simulator')[0]
M_simulator=Aer.backends(name='qasm_simulator')[0]

q=QuantumRegister(3,name='q')
c=ClassicalRegister(3,name='c')
qc=QuantumCircuit(q,c,name='qc')

qc.h(q[0])
qc.iden(q[1])
qc.x(q[2])
qc.measure(q[0],c[0])

print(qc.qasm())

print(qc.data)

print(qc.qregs)

print(qc.cregs)
