
class Constraint():
    def __init__(self, variables):
        self.variables = variables



class CSPVariable():

    def __init__(self, Num, domain):
        self.__Variables = ['x%i' % i for i in range(0, Num, 1)]
        self.__Domain = set([x for x in range(0,domain)])
        self.ConstraintDict: [__Variables, List[Constraint[V, D]]] = {}

    def CopyMethod(self):
        pass

    def __str__(self):
        build = str(self.__Variables) + " " + str(self.__Domain) + " " + str(self.ConstraintDict)
        return build
