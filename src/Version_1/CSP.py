
class CSP: # full csp with variabless, domain, and constraints
	def __init__(self, doms, cons, assignment, nqueens):
		self.doms = doms       # dict mapping queen to its domain, the domain is all the possible assignment it can be placed in
		self.cons = cons       # lisf of lists mapping queen to list of constraints (first item in list if the pair of queens)
		self.assignment = assignment       # the row the queen is assigned to
		self.nqueens = nqueens

	def assign(self, Variable, Value):
		self.assignment[Variable] = Value

	def unassign(self, Variable):
		self.assignment[Variable] = None

	def deleteValue(self, Variable, Value):
		self.doms[Variable].remove(Value)

	def restoreValue(self, Variable, Value):
		self.doms[Variable].append(Value)
		self.doms[Variable].sort()

	def getNextUnassignedVariable(self, varList):
		for i in range(len(self.assignment)):
			if self.assignment[i] == None:
				return i

	def getValFromDomain(self, Variable):
		return (self.doms[Variable][0])

def CSPCallFunction(nqueens):
	doms = {}    # domains of the queens
	assignment = {}    # roassignment the queens will be placed in
	cons = {}    # list of constraints for each queen


	for i in range(0, nqueens): # set list of domains for each queen
		doms.update({i : [x for x in range(0,nqueens)]})
	for i in range(0, nqueens): # set all row assignments to 0 (no row assigned yet)
		assignment.update({i: None})

	for i in range(0, nqueens): # find and set constraints for each pair of queens
		for j in range(i, nqueens):
			if i != j:
				cons.update({(i,j) : set_constraints(i,j, nqueens)})
	csp = CSP(doms, cons, assignment, nqueens)
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
