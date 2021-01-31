"""Stage (canvas) implementation.
"""

from apyscript.expression import expression_file


class Stage:

    def __init__(self):
        """
        Stage (canvas) class.
        """
        expression_file.empty_expression_dir()
