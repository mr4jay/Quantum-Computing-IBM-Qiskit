from qiskit import ClassicalRegister,QuantumRegister,QuantumCircuit,execute,Aer
from qiskit import IBMQ
IBMQ.load_account()
S_simulator=Aer.backends(name='statevector_simulator')[0]
M_simulator=Aer.backends(name='qasm_simulator')[0]

q=QuantumRegister(2)
c=ClassicalRegister(2)
qc=QuantumCircuit(q,c)

qc.h(q[0])
qc.h(q[1])
qc.measure(q[0],c[0])

job=execute(qc,M_simulator,shots=1000)
result=job.result()
result.get_counts(qc)


