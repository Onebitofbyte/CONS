from CSP import CSPCallFunction
from copy import copy, deepcopy
import time

def FCSolver(csp,varList):

	if csp.assignment[csp.nqueens-1]!=None:
		print("YES")
		time.sleep(5)
	Variable = csp.getNextUnassignedVariable(varList)
	Value = csp.getValFromDomain(Variable)

	print("Assigning "+str(Value) + " to Queen Q"+str(Variable))
	FCBranchLeft(csp, varList, Variable, Value)
	FCBranchRight(csp, varList, Variable, Value)

def PruneThisVariable(csp, Variable, Assignment):
	for i in range(Assignment, csp.nqueens-Variable):
		if (Assignment in csp.doms[i]):
			csp.doms[i].remove(Assignment)
	for i in range(Variable, csp.nqueens):
		for j in range(Assignment, csp.nqueens):
			if (Variable == Assignment + (j-i)) or (Variable == Assignment - (j-i)):
				if (i <= j) and (j in csp.doms[i]):
					csp.doms[i].remove(j)


def FCBranchLeft(csp, varList, Variable, Value):
	count=0
	kept_domains = copy(csp.doms)
	csp.assign(Variable, Value)
	PruneThisVariable(csp, Variable, Value)
	if reviseFutureArcs(csp, varList, Variable):
		print("We here "+str(count))
		count+=1
		FCSolver(csp, varList[1:])
	csp.unassign(Variable)
	csp.doms = kept_domains
	#Still need to undo Pruning

	# for i in csp.cons.keys():
	# 	revise(csp, i[0], i[1])

def reviseFutureArcs(csp, varList, Variable):
	consistent = True
	kept_domains = copy(csp.doms)

	for futureVar in varList:
		if (futureVar != Variable):
			#print("Revising "+str(Variable)+ " with "+ str(futureVar))
			consistent = revise(csp, Variable, futureVar)
			if (consistent == False):
				print("FUCK we failed")
				return False
			#time.sleep(5)


	return True




def FCBranchRight(csp, varList, Variable, Value):
	print("Okay we here "+str((Variable,Value)))
	csp.deleteValue(Variable, Value)
	if (not csp.doms[Variable].isEmpty()):
		kept_domains = copy(csp.doms)
		if reviseFutureArcs(csp, varList, Variable):
			FCSolver(csp, varList)
		csp.doms = kept_domains
	restoreValue(Variable, Value)


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
	# print("domain Q"+str(q1)+" is "+str(new_d1))
	# print("domain Q"+str(q2)+" is "+ str(new_d2))
	#csp.doms[q1]=new_d1
	csp.doms[q2]=new_d2
	return ((len(new_d2) > 0) and len(new_d1) > 0)


nqueens = 4
csp = CSPCallFunction(nqueens)
varList=[]
for i in csp.assignment:
	varList.append(i)
FCSolver(csp, varList)

print(csp.doms)
