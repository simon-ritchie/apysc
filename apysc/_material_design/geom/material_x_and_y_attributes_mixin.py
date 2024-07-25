"""The mix-in class implementation for the material design's x and y
coodrinates attributes.
"""


from typing import Union

from apysc._type.number import Number


class MaterialXAndYAttributesMixIn:

    def _set_x_and_y_coordinates(
        self,
        *, x:
        Union[float, Number],
        y: Union[float, Number]) -> None:
        """
        Set the x and y coordinates to instance button.

        Parameters
        ----------
        x : Union[float, Number]
            X-coordinate.
        y : Union[float, Number]
            Y-coordinate.
        """
        from apysc._converter import to_apysc_val_from_builtin
        from apysc._type.variable_name_suffix_utils import (
            get_attr_or_variable_name_suffix,
        )

        self.x = to_apysc_val_from_builtin.get_copied_number_from_builtin_val(
            float_or_num=x,
            variable_name_suffix=get_attr_or_variable_name_suffix(
                instance=self,
                value_identifier="x",
            ),
        )
        self.y = to_apysc_val_from_builtin.get_copied_number_from_builtin_val(
            float_or_num=y,
            variable_name_suffix=get_attr_or_variable_name_suffix(
                instance=self,
                value_identifier="y",
            ),
        )
