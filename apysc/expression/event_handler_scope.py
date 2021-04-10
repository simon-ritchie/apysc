"""Implementations for event handler's expression scope
interfaces.
"""


def enter_event_handler_scope() -> None:
    """
    Enter and set event handler scope setting.
    """
    from apysc.file import file_util
    from apysc.expression import expression_file_util
    file_util.save_plain_txt(
        txt='',
        file_path=expression_file_util.IS_EVENT_HANDLER_SCOPE_FILE_PATH)
