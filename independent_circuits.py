from qiskit import ClassicalRegister,QuantumRegister,QuantumCircuit,Aer
from qiskit import IBMQ
IBMQ.load_account()
S_simulator=Aer.backends(name='statevector_simulator')[0]
M_simulator=Aer.backends(name='qasm_simulator')[0]

q1=QuantumRegister(1,name='q1')
c1=ClassicalRegister(1,name='c1')
qc1=QuantumCircuit(q1,c1,name='qc1')

q2=QuantumRegister(1,name='q2')
c2=ClassicalRegister(1,name='c2')
qc2=QuantumCircuit(q2,c2,name='qc2')

qc1.h(q1[0])
qc2.h(q2[0])

print(qc1.qasm()[36:len(qc1.qasm())])
print(qc2.qasm()[36:len(qc2.qasm())])