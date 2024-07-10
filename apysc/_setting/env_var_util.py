"""Implementations for environment variable related utilities.
"""

import os


def apply_material_icons_import_skipping_setting() -> None:
    """
    Apply the environment variable setting to skip importing Material icons.

    Notes
    -----
    This function needs to call before importing apysc package
    (i.e., `import apysc as ap`).
    """
    os.environ["APYSC_SKIP_MATERIAL_ICONS"] = "1"


def skip_material_icons_importing() -> bool:
    """
    Get a boolean value whether to skip importing Material icons or not.

    Returns
    -------
    result : bool
        If the environment variable is set to skip importing Material icons,
        then this function returns True.
    """
    skip_material_icons: str = os.environ.get("APYSC_SKIP_MATERIAL_ICONS", "")
    try:
        return bool(int(skip_material_icons))
    except ValueError:
        return False
