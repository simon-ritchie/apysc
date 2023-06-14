"""The loop-related utilities implementations.
"""

from typing import Type, Union

from apysc._type.string import String
from apysc._type.int import Int
from apysc._type.boolean import Boolean
from apysc._html.debug_mode import add_debug_info_setting


@add_debug_info_setting(module_name=__name__)
def get_dict_key_for_loop(
    *,
    dict_key_type: Type[Union[str, String, int, Int, bool, Boolean]],
) -> Union[String, Int, Boolean]:
    """
    Get a dictionary key for a loop-related implementation.

    Parameters
    ----------
    dict_key_type : Type[Union[str, String, int, Int, bool, Boolean]]
        A dictionary key type.

    Returns
    -------
    dict_key : Union[String, Int, Boolean]
        An apysc's dictionary key.
    """
    if issubclass(dict_key_type, (str, String)):
        return String._initialize_for_loop_value()
    if issubclass(dict_key_type, (int, Int)):
        return Int._initialize_for_loop_value()
    if issubclass(dict_key_type, (bool, Boolean)):
        return Boolean._initialize_for_loop_value()
    raise TypeError(
        f"Unsupported dictionary key type: {type(dict_key_type).__name__}"
        "\nAcceptable types are: `str`, `ap.String`, `int`, `ap.Int`, `bool`, "
        "or `ap.Boolean`."
    )
