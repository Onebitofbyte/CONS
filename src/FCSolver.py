from CSP import CSPCallFunction
from copy import copy, deepcopy

def FCSolver(csp):
	FCBranchLeft(csp,1,6)


def FCBranchLeft(csp, queen, value):
	for i in csp.cons.keys():
		revise(csp, i[0], i[1])




def revise(csp, q1, q2):
	print(csp.cons[(q1,q2)])
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
	print("domain Q"+str(q1)+" is "+str(new_d1))
	print("domain Q"+str(q2)+" is "+ str(new_d2))
	csp.doms[q1]=new_d1
	csp.doms[q2]=new_d2
	return ((len(new_d2) > 0) and len(new_d1) > 0)



csp = CSPCallFunction(3)
FCSolver(csp)
print(csp.assignment)
print("Next = "+ str(csp.getNextUnassignedVariable()))
