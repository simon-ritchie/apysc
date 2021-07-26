"""Class implementation for the continue.
"""


class Continue:
    """
    The loop continue expression class.

    Notes
    -----
    This class can be instantiated in the with loop statement,
    for example, after the `with ap.For(...):` statement.
    """

    def __init__(self) -> None:
        """
        The loop continue expression class.

        Notes
        -----
        This class can be instantiated in the with loop statement,
        for example, after the `with ap.For(...):` statement.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=Continue):
            from apysc._loop import loop_count
            current_loop_count: int = loop_count.get_current_loop_count()
            if current_loop_count == 0:
                err_msg: str = (
                    'The `Continue` class can be instantiated in the with '
                    'loop statement, for example, after the '
                    '`with ap.For(...):` statement.'
                )
                raise Exception(err_msg)
            ap.append_js_expression(expression='continue;')
