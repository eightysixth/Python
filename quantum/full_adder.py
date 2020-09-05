from qiskit import QuantumCircuit, QuantumRegister, execute, Aer
from qiskit.visualization import plot_histogram


# Full adder circuit
qc = QuantumCircuit(4,4) # 4 qbits, 4 classical bits (output)
qc.x(0)     # For a=0, comment this line. For a=1, leave it.
# qc.x(1)   # For b=0, comment this line. For b=1, leave it.
qc.x(2)     # For c=0, comment this line. For b=1, leave it.
qc.barrier()
qc.ccx(0, 1, 3)
qc.cx(0,1)
qc.ccx(1,2,3)
qc.cx(1,2)
qc.cx(0,1)
qc.barrier()
qc.measure(0,0) # measure qbit 0 into bit 0
qc.measure(1,1) # measure qbit 1 into bit 1
qc.measure(2,2) # measure qbit 2 into bit 2
qc.measure(3,3) # measure qbit 3 into bit 3 --> Carry bit
print(qc.draw())

counts = execute(qc, Aer.get_backend('qasm_simulator')).result().get_counts()
print("Counts")
for i in counts:
    print(i + ':', counts[i])