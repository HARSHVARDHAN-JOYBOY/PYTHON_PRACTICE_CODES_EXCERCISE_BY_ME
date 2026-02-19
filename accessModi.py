class emp:       #access modeifiers are used as convention
    def __init__(self):
        self.__name = "Ram"
a= emp()           #ex of name mangling
#print(a.__name) can not br access directly
print(a._emp__name) #can be access indirectly
#print(a.__dir__()) # Shows all available method 