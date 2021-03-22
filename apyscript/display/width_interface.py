"""Class implementation for witdth interface.
"""

from apyscript.type import Int
from apyscript.type.variable_name_interface import VariableNameInterface


class WidthInterface(VariableNameInterface):

    _width: Int

    def _initialize_width_if_not_initialized(self) -> None:
        """
        Initialize _width attribute if it is not initialized yet.
        """
        if hasattr(self, '_width'):
            return
        self._width = Int(0)

    @property
    def width(self) -> Int:
        """
        Get this instance's width.

        Returns
        -------
        width : Int
            This instance's width.
        """
        from apyscript.type import value_util
        self._initialize_width_if_not_initialized()
        return value_util.get_copy(value=self._width)

    @width.setter
    def width(self, value: Int) -> None:
        """
        Update this instance's width.

        Parameters
        ----------
        value : Int
            Width value to set.
        """
        self.update_width_and_skip_appending_exp(value=value)
        self._append_width_update_expression()

    def _append_width_update_expression(self) -> None:
        """
        Append width updating expression.
        """
        from apyscript.expression import expression_file_util
        from apyscript.html import html_util
        expression: str = (
            f'{self.variable_name}.width({self.width});'
        )
        expression = html_util.wrap_expression_by_script_tag(
            expression=expression)
        expression_file_util.append_expression(
            expression=expression)

    def update_width_and_skip_appending_exp(self, value: Int) -> None:
        """
        Update width value and skip appending expression to file.

        Parameters
        ----------
        value : Int
            Width value to set.
        """
        from apyscript.converter import cast
        from apyscript.validation import size_validation
        self._initialize_width_if_not_initialized()
        value = cast.to_int_from_float(int_or_float=value)
        size_validation.validate_size_is_int(size=value)
        size_validation.validate_size_is_gte_zero(size=value)
        self._width = value
