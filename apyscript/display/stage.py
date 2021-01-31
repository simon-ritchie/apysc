"""Stage (canvas) implementation.
"""

from apyscript.expression import file_util


class Stage:

    def __init__(self):
        """
        Stage (canvas) class.
        """
        file_util.empty_expression_dir()
