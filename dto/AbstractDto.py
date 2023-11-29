import UtilFunctions as Util

class AbstractDto:

    @classmethod
    def initFromDict(cls, dictVals: dict):
        obj = cls()
        for item in dictVals:
            if hasattr(obj, item):
                try:
                    setattr(obj, item, dictVals.get(item))
                except AttributeError: pass
        return obj

    def __dict__(self) -> dict:
        return Util.toDict(self)
