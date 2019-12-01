import qiskit
from qiskit import IBMQ
IBMQ.load_account()
from qiskit import BasicAer
from qiskit.aqua import QuantumInstance
from qiskit.aqua import run_algorithm
from qiskit.aqua.algorithms import DeutschJozsa
from qiskit.aqua.components.oracles import TruthTableOracle

bitstr = '11110000'
oracle = TruthTableOracle(bitstr)

oracle.circuit.draw(output='mpl')

dj = DeutschJozsa(oracle)
backend = BasicAer.get_backend('qasm_simulator')
result = dj.run(QuantumInstance(backend, shots=1024))
print('The truth table {} represents a {} function.'.format(bitstr, result['result']))


bitstr = '11110000'
params = {
    'problem': {
        'name': 'functionevaluation',
    },
    'algorithm': {
        'name': 'DeutschJozsa'
    },
    'oracle': {
        'name': 'TruthTableOracle',
        'bitmaps': [bitstr]
    },
    'backend': {
        'shots': 1024,
    },
}

result_dict = run_algorithm(params, backend=backend)
print('The truth table {} represents a {} function.'.format(bitstr, result_dict['result']))

bitstr = '1' * 32
oracle = TruthTableOracle(bitstr)
dj = DeutschJozsa(oracle)
backend = BasicAer.get_backend('qasm_simulator')
result = dj.run(QuantumInstance(backend, shots=1024))
print('The truth table {} represents a {} function.'.format(bitstr, result['result']))