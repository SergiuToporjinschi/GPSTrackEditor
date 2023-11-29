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