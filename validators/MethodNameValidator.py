import keyword, re

from PySide6.QtGui import QValidator

class MethodNameValidator(QValidator):
    def validate(self, input_str, pos):
        if not input_str:
            return QValidator.State.Acceptable, input_str, pos

        if input_str.isidentifier() and not keyword.iskeyword(input_str):
            return QValidator.State.Acceptable, input_str, pos
        elif re.match(r'[\s+/\-*]', input_str[pos-1]):
            input_str = re.sub(r'[\s+/\-*]+', r'_', input_str)
            return QValidator.State.Acceptable, input_str, pos
        else:
            return QValidator.State.Invalid, input_str, pos