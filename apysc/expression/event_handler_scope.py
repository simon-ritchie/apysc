"""Implementations for event handler's expression scope
interfaces.
"""

import os


def current_scope_is_event_handler() -> bool:
    """
    Get a boolean value whether current scope is an event handler
    one or not.

    Returns
    -------
    result : bool
        If current scope is event handler one, then True will be
        returned
    """
    from apysc.expression import expression_file_util
    if os.path.isfile(expression_file_util.IS_EVENT_HANDLER_SCOPE_FILE_PATH):
        return True
    return False
