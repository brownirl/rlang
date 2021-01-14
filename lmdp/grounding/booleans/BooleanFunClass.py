'''
    Boolean Fun class 
'''
class BooleanExpression:
    def __init__(self, fun):
        self._fun = fun

    def __call__(self, *args):
        return self._fun(*args)
        
    def and_(self, other):
        if(isinstance(other, BooleanExpression)):
            return lambda *args: self.__call__(*args) and other(*args)
        elif (isinstance(other, bool)):
            return lambda *args: self.__call__(*args) and other 
        else:
            raise other.__name__() + " must be a Boolean Fun or bool"
   
    def or_(self, other):
        if(isinstance(other, BooleanExpression)):
            return lambda *args: self.__call__(*args) or other(*args)
        elif (isinstance(other, bool)):
            return lambda *args: self.__call__(*args) or other 
        else:
            raise other.__name__() + " must be a Boolean Fun or bool"
    
    def not_(self):
        return lambda *args: not self.__call__(*args)
        
