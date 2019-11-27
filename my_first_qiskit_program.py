from matplotlib import pyplot as plt
import qiskit
from qiskit import *
from qiskit.visualization import plot_bloch_vector
hello=qiskit.__version__
world=qiskit.__qiskit_version__
print(hello)
print(world)
#print(IBMQ.load_account())
plt.figure()
ax = plt.gca()
ax.quiver([3], [5], angles='xy', scale_units='xy', scale=1)
ax.set_xlim([-1, 10])
ax.set_ylim([-1, 10])
plt.draw()
plt.show()
plot_bloch_vector([1,0,0])
