from qiskit import ClassicalRegister,QuantumRegister,QuantumCircuit,Aer
from qiskit import IBMQ
IBMQ.load_account()
S_simulator=Aer.backends(name='statevector_simulator')[0]
M_simulator=Aer.backends(name='qasm_simulator')[0]

q=QuantumRegister(2,name='q')
c=ClassicalRegister(2,name='c')
qc=QuantumCircuit(q,c,name='qc')

qc.h(q[0])
qc.h(q[1])
qc.measure(q[0],c[0])

inst=qc.data[1]

print(qc.qasm()[36:len(qc.qasm())])
del qc.data[1]
print(qc.qasm()[36:len(qc.qasm())])
qc.data.append(inst)
print(qc.qasm()[36:len(qc.qasm())])
qc.data.insert(0,inst)
print(qc.qasm()[36:len(qc.qasm())])