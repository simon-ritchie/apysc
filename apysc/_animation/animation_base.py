"""Base class implementation for the animation.
"""

from abc import ABC
from abc import abstractmethod
from typing import Any
from typing import Callable
from typing import Generic
from typing import Optional
from typing import TypeVar
from typing import Union

import apysc as ap
from apysc._animation.easing import Easing
from apysc._event.custom_event_interface import CustomEventInterface
from apysc._type.variable_name_interface import VariableNameInterface

_T = TypeVar('_T', bound=VariableNameInterface)
_O = TypeVar('_O')
_AnimationEvent = Any
_Handler = Callable[[_AnimationEvent, _O], None]


class AnimationBase(
        VariableNameInterface, CustomEventInterface, Generic[_T], ABC):

    _target: _T
    _duration: ap.Int
    _delay: ap.Int
    _easing: Easing
    _started: ap.Boolean

    def __init__(self, variable_name: str) -> None:
        """
        Base class for each animation setting.

        Parameters
        ----------
        variable_name : str
            Variable name.
        """
        self.variable_name = variable_name
        self._started = ap.Boolean(False)

    @abstractmethod
    def _get_animation_func_expression(self) -> str:
        """
        Get a animation function expression.
        """

    def _set_basic_animation_settings(
            self,
            target: _T,
            duration: Union[int, ap.Int] = 3000,
            delay: Union[int, ap.Int] = 0,
            easing: Easing = Easing.LINEAR) -> None:
        """
        Set the basic animation settings.

        Parameters
        ----------
        target : VariableNameInterface
            A target instance of the animation target
            (e.g., `DisplayObject` instance).
        duration : int or Int, default 3000
            Milliseconds before an animation ends.
        delay : int or Int, default 0
            Milliseconds before an animation starts.
        easing : Easing, default Easing.LINEAR
            Easing setting. If None, Linear calculation is used.
        """
        with ap.DebugInfo(
                callable_=self._set_basic_animation_settings,
                locals_=locals(),
                module_name=__name__, class_=AnimationBase):
            from apysc._converter import to_apysc_val_from_builtin
            self._target = target
            self._duration = to_apysc_val_from_builtin.\
                get_copied_int_from_builtin_val(integer=duration)
            self._delay = to_apysc_val_from_builtin.\
                get_copied_int_from_builtin_val(integer=delay)
            self._easing = easing

    def start(self) -> 'AnimationBase':
        """
        Start an animation with current settings.

        Returns
        -------
        self : AnimatonBase
            This instance.

        References
        ----------
        - AnimationBase class start interface
            - https://simon-ritchie.github.io/apysc/animation_base_start.html
        """
        with ap.DebugInfo(
                callable_=self.start, locals_=locals(),
                module_name=__name__, class_=AnimationBase):
            expression: str = (
                f'{self._target.variable_name}'
                '\n  .animate({'
                f'\n    duration: {self._duration.variable_name},'
                f'\n    delay: {self._delay.variable_name}}})'
                f'\n  .ease({self._easing.value})'
            )
            expression += self._get_animation_complete_handler_expression()
            animation_expresssion: str = self._get_animation_func_expression()
            expression += animation_expresssion
            ap.append_js_expression(expression=expression)
            self._started.value = True
        return self

    def _get_animation_complete_handler_expression(self) -> str:
        """
        Get a expression of the animation complete handlers setting.

        Returns
        -------
        expression : str
            Target expression string.
            e.g., '\n  .after(handler_name)'

        Notes
        -----
        If multiple handlers are registered, then multiple lines
        expression will be returned.
        """
        from apysc._event.custom_event_type import CustomEventType
        event_type: str = CustomEventType.ANIMATION_COMPLETE.value
        self._initialize_custom_event_handlers_if_not_initialized(
            custom_event_type_str=event_type)
        if event_type not in self._custom_event_handlers:
            return ''
        expression: str = ''
        for handler_name in self._custom_event_handlers[event_type].keys():
            expression += f'\n  .after({handler_name})'
        return expression

    def animation_complete(
            self, handler: _Handler[_O],
            options: Optional[_O] = None) -> 'AnimationBase':
        """
        Add a animation complete event listener setting.

        Notes
        -----
        This interface can only be used before an animation start.

        Parameters
        ----------
        handler : _Handler
            A callable will be called when an animation is complete.
        options : dict or None, default None
            Optional arguments dictionary to be passed to a handler.

        Returns
        -------
        self : AnimatonBase
            This instance.

        Raises
        ------
        Exception
            If this interface is called after an animation start.

        References
        ----------
        - AnimationBase class animation_complete interface document
            - https://simon-ritchie.github.io/apysc/animation_complete.html
        - About the handler options’ type document
            - https://bit.ly/39tnYxC
        """
        with ap.DebugInfo(
                callable_=self.animation_complete, locals_=locals(),
                module_name=__name__, class_=AnimationBase):
            from apysc._event.custom_event_type import CustomEventType
            from apysc._validation.handler_options_validation import \
                validate_options_type
            self._validate_animation_not_started()
            validate_options_type(options=options)
            e: ap.AnimationEvent[_T] = ap.AnimationEvent(this=self)
            in_handler_head_expression: str = \
                self._get_complete_event_in_handler_head_expression()
            self.bind_custom_event(
                custom_event_type=CustomEventType.ANIMATION_COMPLETE,
                handler=handler,
                e=e,
                options=options,
                in_handler_head_expression=in_handler_head_expression)
            return self

    @abstractmethod
    def _get_complete_event_in_handler_head_expression(self) -> str:
        """
        Get an expression to be inserted into the complete event
        handler's head.
        """

    def _validate_animation_not_started(self) -> None:
        """
        Validate whether an animation hasn't already been started.

        Raises
        ------
        Exception
            If an animation has already been started.
        """
        if not self._started._value:
            return
        raise Exception(
            'This interface can not be called after the animation '
            'is started.')

    @property
    def target(self) -> _T:
        """
        Get an animation target instance.

        Returns
        -------
        target : VariableNameInterface
            An animation target instance.

        References
        ----------
        - AnimationBase class target property interface document
            - https://simon-ritchie.github.io/apysc/animation_base_target.html
        """
        return self._target
