from qiskit import ClassicalRegister,QuantumRegister,QuantumCircuit,Aer
from qiskit.tools.visualization import circuit_drawer
import math as m
from qiskit import IBMQ
IBMQ.load_account()
S_simulator=Aer.backends(name='statevector_simulator')[0]
M_simulator=Aer.backends(name='qasm_simulator')[0]

q=QuantumRegister(1,name='q')
c=ClassicalRegister(1,name='c')
qc=QuantumCircuit(q,c,name='qc')

qc.rx(m.pi/4,q[0])
print(circuit_drawer(qc))
qc.ry(m.pi/4,q[0])
print(circuit_drawer(qc))
qc.rz(m.pi/4,q[0])
print(circuit_drawer(qc))