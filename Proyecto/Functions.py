import numpy as np
from qiskit import QuantumCircuit
from sympy import Matrix

def ImprimirMatriz(M):
    display(Matrix(M))

def CapaHadamard(n_qubits):
    qc = QuantumCircuit(n_qubits)
    qc.h([i for i in range(n_qubits)])
    
    return qc
