class CSPVariables():


    def __init__(self, Num, domain):
        self.__name = ['x%i' % i for i in range(0, Num, 1)]
        self.__domain = set([x for x in range(0,domain)])

#def addConstraints(self):

    def __str__(self):
        build = str(self.__name) + " " + str(self.__domain)
        return build
