from CSP import CSPCallFunction
from copy import copy, deepcopy

def FCSolver(csp):
	FCBranchLeft(csp,1,6)


def FCBranchLeft(csp, queen, value):
	csp.assign(queen,value)
	print(revise(csp,0,1))
	print(csp.doms[0])
	print(csp.doms[1])

def revise(csp, q1, q2):
	revised = False
	cons = copy(csp.cons[(q1,q2)])
	print(cons)
	c = []
	for i in cons:
		if i[0] not in c:
			c.append(i[0])
	csp.doms[q1]=c
	if c == []:
		return False
	else:
		csp.doms[q1]=c
		return True


csp = CSPCallFunction(3)
FCSolver(csp)
