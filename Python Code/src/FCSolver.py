from CSP import CSPCallFunction
from copy import copy, deepcopy
import sys

def FCSolver(csp, varList):
# Method that performs 2-way forward checking to solve a given N-Queens CSP
# Parameters (CSP, VarList)
# Returns: None
	if csp.assignment[csp.nqueens-1]!=None:
		print("Our Solution Assignments : "+str(csp.assignment))
		sys.exit()
	Variable = csp.getNextUnassignedVariable(varList)
	Value = csp.getValFromDomain(Variable)
	FCBranchLeft(csp, varList, Variable, Value) # Left Branch for equality (=) prune
	FCBranchRight(csp, varList, Variable, Value) # Right Branch for not equal (≠) prune

def PruneThisVariable(csp, Variable, Assignment):
# Method used to eliminate all the domains from a given Variable and Assignment
# Parameters (CSP:CSP, Variable:Integer, Assignment:Integer)
# Returns: None
	for i in range(Variable+1, csp.nqueens): # prunes Column
		if (Assignment in csp.doms[i]):
			csp.doms[i].remove(Assignment)
	for i in range(Variable+1, csp.nqueens):# prunes diagonal
		for j in range(Assignment+1, csp.nqueens):
			if (Variable == Assignment + (j-i)) or (Variable == Assignment - (j-i)):
				if (i <= j) and (j in csp.doms[i]) and (Assignment != csp.doms[i]):
					csp.doms[i].remove(j)


def FCBranchLeft(csp, varList, Variable, Value):
# Method for equality (=) prune, assignment the Variable with Value
# Parameters: (CSP: CSP, varList: array of Integer, Variable: Integer, Value: Integer)
# return: None
	print("Left Branch now Q"+str(Variable)+"="+str(Value))
	kept_domains = deepcopy(csp.doms) # Copies CSP domain for when to backtrack
	csp.assign(Variable, Value)
	PruneThisVariable(csp, Variable, Value)
	if reviseFutureArcs(csp, varList, Variable): # calls reviseFutureArcs
		print("Revised domains:")
		for i in range(len(csp.doms)):
			print("Q"+str(i)+": "+str(csp.doms[i]))
		FCSolver(csp, varList[1:]) # No domain wipeout, calls next variable in varList
	csp.unassign(Variable) # Backtracking, unassigning variable and returning to previous domains
	csp.doms = kept_domains


def reviseFutureArcs(csp, varList, Variable):
# Method that revises the all future set of arcs in varList from an assignment
#Parameters (CSP:CSP, varList: Array of Integer, Variable: Integer)
#return: Boolean
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
# Method for not equal (≠) prune, assignment the Variable with Value
# Parameters: (CSP: CSP, varList: array of Integer, Variable: Integer, Value: Integer)
# return: None
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
# Method that takes a single arc and revises it, also updates domains from constraints
# Parameters (CSP: CSP, q1:Integer, q2:Integer)
# Returns: Boolean

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
					applied_constraints_d1.append(Constraint) # Checks all constraint still connected to the first queen
	for Constraint in applied_constraints_d1:
		if (Constraint[1] in d2) and (Constraint[0] in d1): # Checks if secound queen is connected
			if (Constraint[0] not in new_d1): # Creates the new domains
				new_d1.append(Constraint[0])
			if (Constraint[1] not in new_d2):
				new_d2.append(Constraint[1])
	new_d2.sort()
	csp.doms[q2]=new_d2
	return ((len(new_d2) > 0) and len(new_d1) > 0)


#Main() Method
nqueens = 6
csp = CSPCallFunction(nqueens)

varList=[]
for i in csp.assignment: # Creates varList of starting queens variable
	varList.append(i)
FCSolver(csp, varList)
