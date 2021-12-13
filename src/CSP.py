
class CSP: # full csp with variabless, domain, and constraints
	def __init__(self, doms, cons, assignment):
		self.doms = doms       # dict mapping queen to its domain, the domain is all the possible assignment it can be placed in
		self.cons = cons       # lisf of lists mapping queen to list of constraints (first item in list if the pair of queens)
		self.assignment = assignment       # the row the queen is assigned to

def CSPCallFunction(nqueens):
	doms = {}    # domains of the queens
	assignment = {}    # roassignment the queens will be placed in
	cons = {}    # list of constraints for each queen


	for i in range(0, nqueens): # set list of domains for each queen
		doms.update({i : [x for x in range(0,nqueens)]})
	for i in range(0, nqueens+1): # set all row assignments to 0 (no row assigned yet)
		assignment.update({i: 0})

	for i in range(0, nqueens): # find and set constraints for each pair of queens
		for j in range(i, nqueens):
			if i != j:
				cons.update({(i,j) : set_constraints(i,j, nqueens)})
	csp = CSP(doms, cons, assignment)
	return csp

def set_constraints(q1, q2, nqueens): # q2 represents the columns # This Can move to FCSolver Later 
	row2 = 0
	dcol = abs(q1 - q2)
	ListOfConstraints = []
	for row1 in range(0, nqueens):
		for row2 in range(0, nqueens):
			drow = abs(row1 - row2)
			if row1 != row2 and q1 != q2 and drow != dcol:
				ListOfConstraints.append([row1, row2])
	return ListOfConstraints

csp = CSPCallFunction(6)
print(csp.doms)

for i in csp.cons:
    print(i)
    print(csp.cons[i])
#print(csp.cons)
