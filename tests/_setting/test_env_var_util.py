import os

from apysc._setting import env_var_util
from apysc._testing.testing_helper import apply_test_settings


@apply_test_settings()
def test_apply_material_icons_import_skipping_setting() -> None:
    os.environ["APYSC_SKIP_MATERIAL_ICONS"] = ""
    env_var_util.apply_material_icons_import_skipping_setting()
    assert os.environ["APYSC_SKIP_MATERIAL_ICONS"] == "1"
    os.environ["APYSC_SKIP_MATERIAL_ICONS"] = ""


@apply_test_settings()
def test_skip_material_icons_importing() -> None:
    os.environ["APYSC_SKIP_MATERIAL_ICONS"] = ""
    result: bool = env_var_util.skip_material_icons_importing()
    assert not result

    os.environ["APYSC_SKIP_MATERIAL_ICONS"] = "test"
    result = env_var_util.skip_material_icons_importing()
    assert not result

    env_var_util.apply_material_icons_import_skipping_setting()
    result = env_var_util.skip_material_icons_importing()
    assert result
    os.environ["APYSC_SKIP_MATERIAL_ICONS"] = ""
