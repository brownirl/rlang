'''
    Boolean Fun class 
'''
class BooleanFun:
    def __init__(self, fun):
        self.__fun = fun

    def __call__(self, *args):
        return self.__fun(*args)
        
    def __and__(self, other):
        if(isinstance(other, BooleanFun)):
            return lambda *args: self.__call__(*args) and other(*args)
        elif (isinstance(other, bool)):
            return lambda *args: self.__call__(*args) and other 
        else:
            raise other.__name__() + " must be a Boolean Fun or bool"
   
    def __or__(self, other):
        if(isinstance(other, BooleanFun)):
            return lambda *args: self.__call__(*args) or other(*args)
        elif (isinstance(other, bool)):
            return lambda *args: self.__call__(*args) or other 
        else:
            raise other.__name__() + " must be a Boolean Fun or bool"
    
    def __invert__(self):
        if(isinstance(other, BooleanFun)):
            return lambda *args: not self.__call__(*args)
        else:
            raise other.__name__() + " must be a Boolean Fun or bool"
