"""The mix-in class for the `_add_to_parent` method.
"""

from typing import Optional

from typing_extensions import final

from apysc._display.child_mixin import ChildMixIn
from apysc._display.display_object import DisplayObject
from apysc._html.debug_mode import add_debug_info_setting
from apysc._validation import arg_validation_decos


class AddToParentMixIn:
    @final
    @arg_validation_decos.is_display_object_container(
        arg_position_index=1, optional=True
    )
    @add_debug_info_setting(module_name=__name__)
    def _add_to_parent(self, *, parent: Optional[ChildMixIn]) -> None:
        """
        Add this instance to a specified parent instance.

        Parameters
        ----------
        parent : Optional[ChildMixIn]
            A parent instance. If the specified value is None,
            this interface uses a stage instance.
        """
        from apysc._display.stage import get_stage

        if not isinstance(self, DisplayObject):
            raise TypeError(
                "This method can only be called by a DisplayObject class instance."
            )

        if parent is None:
            parent = get_stage()
        parent.add_child(child=self)
