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
