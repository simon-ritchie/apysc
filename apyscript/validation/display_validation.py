"""Each display's validation implementations.
"""


def validate_stage(stage):
    """
    Validate whether the specified instance is Stage type or not.

    Parameters
    ----------
    stage : Stage
        Stage instance to check.

    Raises
    ------
    ValueError
        If specified instance is not stage type.
    """
    from apyscript.display.stage import Stage
    if isinstance(stage, Stage):
        return
    raise ValueError(
        f'Specified instance is not stage type: {type(stage)}')
