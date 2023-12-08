import UtilFunctions as Util

class CalcColumnDto:
    def __init__(self, name: str, expression:str, active:bool=False) -> None:
        self.expression = Util.beautifyExpression(expression)
        self.active = active
        self.name = name
        pass

    def __getstate__(self):
        state = self.__dict__.copy()
        state['active'] = False
        return state