import re, json
from typing import Callable, List
import importlib


nonPrivate:Callable = lambda item: item[0] != '_'

def getClassPublicAttributes(type: type, filterFunction: Callable = nonPrivate) -> list[str]:
    """
        returns a list[str] with attribute names of given class, filtered by a given function
        param:
            type (type): class to iterate
            filterFunction (Callable(item)): a lambda function to evaluate if the attribute is included or not
                default value: attributes not starting with _ (non private)
    """
    result = []
    for item in vars(type):
        if filterFunction(item) and not callable(getattr(type, item, None)):
            result.append(item)
    return result

def iterateClassPublicAttributes(type: type, filterFunction: Callable = nonPrivate) -> None:
    """
        Iterate attributes of given type and calls yield with the string representing the attribute name
        param:
            type (type): class to iterate
            filterFunction (Callable(item)): a lambda function to evaluate if the attribute is included or not
                default value: attributes not starting with _ (non private)
    """
    for item in vars(type) :
        if filterFunction(item) and not callable(getattr(type, item, None)):
            yield item

def buildAttributeExpression(attrName: str, exp:str) -> str:
    """
        Validates a boolean expression and is decorating it with attribute name
        param:
            attrName (str): attribute to be used in expression
            expr     (str): logical expression
        returns:
            logical expression for a specific attribute
    """
    if exp is None or len(exp.strip()) <= 0: return None

    matchSingleExprPattern = r'^(?P<operator><|>|<>|!=|=!|==|<=|>=|=)(?P<value>\d+(\.\d+)?)$'
    matchGeneralExprPattern = r'^(?!.*(?:\|\||&&))(?=.*[|&])[^|&].*[^|&]$'
    splitPattern = r'(\||\&)'

    attrName = attrName.strip()
    exp = exp.strip()

    if re.match(matchGeneralExprPattern, exp) is None: return None

    splitted:list[str] = re.split(splitPattern, exp)

    index = 0
    while index < len(splitted):
        if re.match(matchSingleExprPattern, splitted[index]) is not None:
            splitted.insert(index, attrName)
            index += 1
        index += 1
    splitted
    return ''.join(splitted)


class toDictJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if obj.__dict__ is None: raise "Cannot serialize to JSON, NO __dict__ method!!"
        return obj.__dict__()

def toDict(obj) -> dict:
    result = {}
    for i in iterateClassPublicAttributes(type(obj)):
        val = getattr(obj, i)
        if isinstance(val, List):
            result[i]= []
            for item in val:
                result[i].append(toDict(item))
        else:
            result[i] = getattr(obj, i)
    result['__type__'] = type(obj).__name__
    return result

def fromDictJSONDecoder(obj) -> any:
    # if jsonStr is not None and len(jsonStr.strip()): return None
    result = None
    module = importlib.import_module('dto')
    if '__type__' in obj and hasattr(module, obj['__type__']):
        clsName = obj['__type__']
        if hasattr(module, clsName):
            initFrom = getattr(getattr(module, clsName), 'initFromDict')
            if initFrom and callable(initFrom):
                result = initFrom(obj)
    return result