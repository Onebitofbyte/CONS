from CSP import CSPCallFunction
from copy import copy, deepcopy
import time
import sys


def FCSolver(csp, varList):
	print("Assignment = :" +str(csp.assignment))
	if csp.assignment[csp.nqueens-1]!=None:
		print("Our Solution Assignments : "+str(csp.assignment))
		sys.exit()
	Variable = csp.getNextUnassignedVariable(varList)
	Value = csp.getValFromDomain(Variable)

	FCBranchLeft(csp, varList, Variable, Value)
	FCBranchRight(csp, varList, Variable, Value)

def PruneThisVariable(csp, Variable, Assignment):
	for i in range(Variable+1, csp.nqueens):
		if (Assignment in csp.doms[i]):
			csp.doms[i].remove(Assignment)
	for i in range(Variable+1, csp.nqueens):
		for j in range(Assignment+1, csp.nqueens):
			if (Variable == Assignment + (j-i)) or (Variable == Assignment - (j-i)):
				if (i <= j) and (j in csp.doms[i]) and (Assignment != csp.doms[i]):
					csp.doms[i].remove(j)


def FCBranchLeft(csp, varList, Variable, Value):
	print("Left Branch now Q"+str(Variable)+"="+str(Value))
	thisLevel = deepcopy(csp)
	kept_domains = deepcopy(csp.doms)
	csp.assign(Variable, Value)
	PruneThisVariable(csp, Variable, Value)
	if reviseFutureArcs(csp, varList, Variable):
		print("Revised domains:")
		for i in range(len(csp.doms)):
			print("Q"+str(i)+": "+str(csp.doms[i]))
		FCSolver(csp, varList[1:])
	csp.unassign(Variable)
	csp.doms = kept_domains

def reviseFutureArcs(csp, varList, Variable):
	consistent = True
	kept_domains = copy(csp.doms)
	for futureVar in varList:
		if (futureVar != Variable):
			consistent = revise(csp, Variable, futureVar)
			if (consistent == False):
				print("Domain Wipeout")
				return False
	return True

def FCBranchRight(csp, varList, Variable, Value):
	print("Right Branch now Q"+str(Variable)+"!="+str(Value))
	csp.deleteValue(Variable, Value)
	if (csp.doms[Variable]):
		kept_domains = deepcopy(csp.doms)
		if reviseFutureArcs(csp, varList, Variable):
			print("Revised domains:")
			for i in range(len(csp.doms)):
				print("Q"+str(i)+": "+str(csp.doms[i]))
			FCSolver(csp, varList)
		csp.doms = kept_domains
	csp.restoreValue(Variable, Value)


def revise(csp, q1, q2):
	d1 = copy(csp.doms[q1])
	d2 = copy(csp.doms[q2])
	cons = copy(csp.cons[(q1,q2)])
	new_d1 = []
	new_d2 = []

	applied_constraints_d1 = []

	for i in d1:
		for Constraint in cons:
			if (i == Constraint[0]) and (i not in new_d1):
				if (Constraint not in applied_constraints_d1):
					applied_constraints_d1.append(Constraint)
	for Constraint in applied_constraints_d1:
		if (Constraint[1] in d2) and (Constraint[0] in d1):
			if (Constraint[0] not in new_d1):
				new_d1.append(Constraint[0])
			if (Constraint[1] not in new_d2):
				new_d2.append(Constraint[1])
	new_d2.sort()
	csp.doms[q2]=new_d2
	return ((len(new_d2) > 0) and len(new_d1) > 0)

nqueens = 6
csp = CSPCallFunction(nqueens)
varList=[]
for i in csp.assignment:
	varList.append(i)
FCSolver(csp, varList)
