class RLangSemanticError(Exception):
    pass


class AlreadyBoundError(RLangSemanticError):
    def __init__(self, variable_name):
        self.message = f"LMDP object '{variable_name}' is already bound"
        super().__init__(self.message)


class UnknownVariableError(RLangSemanticError):
    def __init__(self, variable_name):
        self.message = f"Unknown variable '{variable_name}'"
        super().__init__(self.message)