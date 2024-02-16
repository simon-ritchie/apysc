import apysc as ap
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings
from tests._material_design.icon.material_icons_common import assert_constructor


class TestMaterialGTranslateIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        assert_constructor(
            icon_class=ap.MaterialGTranslateIcon,
            expected_variable_name=var_names.MATERIAL_G_TRANSLATE_ICON,
        )
