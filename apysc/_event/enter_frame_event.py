"""Class implementation for the enter frame event.
"""

from typing import Generic
from typing import TypeVar

from typing_extensions import final

from apysc._event.event import Event
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._validation import arg_validation_decos

Target = TypeVar("Target", bound=VariableNameMixIn)


class EnterFrameEvent(Event[Target], Generic[Target]):
    """
    Enter frame event class.
    """

    @final
    @arg_validation_decos.is_variable_name_interface_type(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def __init__(self, *, this: Target) -> None:
        """
        Enter frame event class.

        Parameters
        ----------
        this : VariableNameMixIn
            An instance which a listening event.
        """
        from apysc._expression import var_names

        super(EnterFrameEvent, self).__init__(
            this=this,
            type_name=var_names.ENTER_FRAME_EVENT,
        )
