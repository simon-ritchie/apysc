"""Mix-in class implementation to disable the Python built-in's iteration.
"""


class PyBuiltInIterDisablingMixIn:
    def __iter__(self) -> None:
        """
        The method for the Python built-in's iteration.

        Raises
        ------
        TypeError
            This method always raises a `TypeError` exception.
        """
        raise TypeError(
            f"This instance's type ({type(self).__name__}) does not support "
            "Python's built-in iteration."
            "\nPlease use the `with ap.For` instead."
        )
