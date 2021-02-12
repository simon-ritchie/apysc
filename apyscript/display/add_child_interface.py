"""Class implementation for add_child interface.
"""

from typing import List

from apyscript.display.display_object import DisplayObject
from apyscript.validation import display_validation


class AddChildInterface:

    _childs: List[DisplayObject]

    def add_child(self, child: DisplayObject) -> None:
        """
        Add display object child to this object.

        Parameters
        ----------
        child : DisplayObject
            Child object to add.
        """
        display_validation.validate_display_object(display_object=child)
        self._childs.append(child)
