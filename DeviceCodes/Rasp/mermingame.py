# Importation du système de création de circuit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister

# Importation des simulateurs

from qiskit_aer import StatevectorSimulator

import random

# Note : On considère les qubits 0,1 à Alice et 2,3 à Bob, même chose pour les
# registres classiques, 0 à 2 pour Alice, 3 à 5 pour Bob.

# circMod(lin : int, col : int, qregister) : Prends trois entiers et un
# circuit en entrée. Si player < 1 ou > 2, lin <0 ou > 2, col < 0 ou > 2, cela déclenche une erreur, sinon
# modifie le circuit pour
# classiques.

def circModA(lin : int, col : int, qreg, wfunc):
    creg = ClassicalRegister(1)
    circ = QuantumCircuit(qreg, creg)
    circ.initialize(wfunc)


    if lin == 0 :
        if col == 0 :
            # 0,0 Sz x I
            circ.cx(qreg[0], qreg[4])
            circ.measure(qreg[4],creg[0])
            circ.reset(qreg[4])

        if col == 1 :

            # 0,1 I x Sx
            circ.h(qreg[1])
            circ.cx(qreg[1],qreg[4])
            circ.measure(qreg[4],creg[0])
            circ.h(qreg[1])
            circ.reset(qreg[4])

        if col == 2 :

            # 0,2 Sz x Sx
            circ.h(qreg[1])
            circ.cx(qreg[0],qreg[4])
            circ.cx(qreg[1],qreg[4])
            circ.measure(qreg[4],creg[0])
            circ.h(qreg[1])
            circ.reset(qreg[4])

    if lin == 1 :

        if col == 0 :
            # 1,0 I x Sz
            circ.cx(qreg[1],qreg[4])
            circ.measure(qreg[4],creg[0])
            circ.reset(qreg[4])

        if col == 1 :
            # 1,1 Sx x I
            circ.h(qreg[0])
            circ.cx(qreg[0],qreg[4])
            circ.measure(qreg[4],creg[0])
            circ.h(qreg[0])
            circ.reset(qreg[4])

        if col == 2 :
            # 1,2 Sx x Sz
            circ.h(qreg[0])
            circ.cx(qreg[0],qreg[4])
            circ.cx(qreg[1],qreg[4])
            circ.measure(qreg[4],creg[0])
            circ.h(qreg[0])
            circ.reset(qreg[4])

    if lin == 2 :

        if col == 0 :
            # 2,0 -Sz x Sz
            circ.x(qreg[0])
            circ.cx(qreg[0],qreg[4])
            circ.cx(qreg[1],qreg[4])
            circ.measure(qreg[4],creg[0])
            circ.x(qreg[0])
            circ.reset(qreg[4])

        if col == 1 :
            # 2,1 -Sx x Sx
            circ.h(qreg[0])
            circ.x(qreg[0])
            circ.h(qreg[1])
            circ.cx(qreg[0],qreg[4])
            circ.cx(qreg[1],qreg[4])
            circ.measure(qreg[4],creg[0])
            circ.h(qreg[1])
            circ.x(qreg[0])
            circ.h(qreg[0])
            circ.reset(qreg[4])

        if col == 2 :
            # 2,2 -Sy x Sy
            circ.sdg(qreg[0])
            circ.h(qreg[0])
            circ.x(qreg[0])
            circ.sdg(qreg[1])
            circ.h(qreg[1])
            circ.cx(qreg[0],qreg[4])
            circ.cx(qreg[1],qreg[4])
            circ.measure(qreg[4],creg[0])
            circ.h(qreg[1])
            circ.s(qreg[1])
            circ.x(qreg[0])
            circ.h(qreg[0])
            circ.s(qreg[0])
            circ.reset(qreg[2])
    
    return circ

def circModB(lin : int, col : int, qreg, wfunc):
    creg = ClassicalRegister(1)
    circ = QuantumCircuit(qreg, creg)
    circ.initialize(wfunc)


    if lin == 0 :
        if col == 0 :
            # 0,0 Sz x I
            circ.cx(qreg[2], qreg[5])
            circ.measure(qreg[5],creg[0])
            circ.reset(qreg[5])

        if col == 1 :

            # 0,1 I x Sx
            circ.h(qreg[3])
            circ.cx(qreg[3],qreg[5])
            circ.measure(qreg[3],creg[0])
            circ.h(qreg[3])
            circ.reset(qreg[5])

        if col == 2 :

            # 0,2 Sz x Sx
            circ.h(qreg[3])
            circ.cx(qreg[2],qreg[5])
            circ.cx(qreg[3],qreg[5])
            circ.measure(qreg[5],creg[0])
            circ.h(qreg[3])
            circ.reset(qreg[5])

    if lin == 1 :

        if col == 0 :
            # 1,0 I x Sz
            circ.cx(qreg[3],qreg[5])
            circ.measure(qreg[5],creg[0])
            circ.reset(qreg[5])

        if col == 1 :
            # 1,1 Sx x I
            circ.h(qreg[2])
            circ.cx(qreg[2],qreg[5])
            circ.measure(qreg[5],creg[0])
            circ.h(qreg[2])
            circ.reset(qreg[5])

        if col == 2 :
            # 1,2 Sx x Sz
            circ.h(qreg[2])
            circ.cx(qreg[2],qreg[5])
            circ.cx(qreg[3],qreg[5])
            circ.measure(qreg[5],creg[0])
            circ.h(qreg[2])
            circ.reset(qreg[5])

    if lin == 2 :

        if col == 0 :
            # 2,0 -Sz x Sz
            circ.x(qreg[2])
            circ.cx(qreg[2],qreg[5])
            circ.cx(qreg[3],qreg[5])
            circ.measure(qreg[5],creg[0])
            circ.x(qreg[2])
            circ.reset(qreg[5])

        if col == 1 :
            # 2,1 -Sx x Sx
            circ.h(qreg[2])
            circ.x(qreg[2])
            circ.h(qreg[3])
            circ.cx(qreg[2],qreg[5])
            circ.cx(qreg[3],qreg[5])
            circ.measure(qreg[5],creg[0])
            circ.h(qreg[3])
            circ.x(qreg[2])
            circ.h(qreg[2])
            circ.reset(qreg[5])

        if col == 2 :
            # 2,2 -Sy x Sy
            circ.sdg(qreg[2])
            circ.h(qreg[2])
            circ.x(qreg[2])
            circ.sdg(qreg[3])
            circ.h(qreg[3])
            circ.cx(qreg[2],qreg[5])
            circ.cx(qreg[3],qreg[5])
            circ.measure(qreg[5],creg[0])
            circ.h(qreg[3])
            circ.s(qreg[3])
            circ.x(qreg[2])
            circ.h(qreg[2])
            circ.s(qreg[2])
            circ.reset(qreg[5])
    
    return circ

def circ_init() :
    simulator = StatevectorSimulator()
    reg = QuantumRegister(6)
    circuit = QuantumCircuit(reg)
    circuit.h(reg[0])
    circuit.h(reg[1])
    circuit.cx(reg[0],reg[2])
    circuit.cx(reg[1],reg[3])
    job = simulator.run(circuit, shots=1)
    res = job.result()
    wfunc = res.get_statevector()
    return wfunc, reg, simulator

def process(lin : int, col : int, func, reg, wfunc, simulator) :
    circ = func(lin, col, reg, wfunc)
    job = simulator.run(circ, shots=1)
    res = job.result()
    wfunc = res.get_statevector()
    count = res.get_counts()
    bit = list(count.keys())[0]
    return wfunc, bit


class Game:
    def __init__(self):
        self.alice = random.randrange(3)
        self.bob = random.randrange(3)
        self.wfunc, self.reg, self.simulator = circ_init()

    def getAlice(self):
        return self.alice
    def getBob(self):
        return self.bob
    def getAliceMeasure(self, lin, col):
        self.wfunc, bit = process(lin, col, circModA, self.reg, self.wfunc, self.simulator)
        return bit
    def getBobMeasure(self, lin, col):
        self.wfunc, bit = process(lin, col, circModB, self.reg, self.wfunc, self.simulator)
        return bit