"""Class implementation for the continue.
"""

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting


class Continue:
    """
    The loop continue expression class.

    Notes
    -----
    This class can be instantiated in the with loop statement,
    for example, after the `with ap.For(...):` statement.

    References
    ----------
    - Continue
        - https://simon-ritchie.github.io/apysc/en/continue.html

    Examples
    --------
    >>> import apysc as ap
    >>> arr: ap.Array = ap.Array(range(3))
    >>> with ap.For(arr) as i:
    ...     with ap.If(i == 1):
    ...         _ = ap.Continue()
    ...
    """

    @final
    @add_debug_info_setting(module_name=__name__)
    def __init__(self) -> None:
        """
        The loop continue expression class.

        Notes
        -----
        This class can be instantiated in the with loop statement,
        for example, after the `with ap.For(...):` statement.

        References
        ----------
        - Continue
            - https://simon-ritchie.github.io/apysc/en/continue.html

        Examples
        --------
        >>> import apysc as ap
        >>> arr: ap.Array = ap.Array(range(3))
        >>> with ap.For(arr) as i:
        ...     with ap.If(i == 1):
        ...         _ = ap.Continue()
        ...
        """
        import apysc as ap
        from apysc._loop import loop_count

        current_loop_count: int = loop_count.get_current_loop_count()
        if current_loop_count == 0:
            err_msg: str = (
                "The `Continue` class can be instantiated in the with "
                "loop statement, for example, after the "
                "`with ap.For(...):` statement."
            )
            raise Exception(err_msg)
        ap.append_js_expression(expression="continue;")
