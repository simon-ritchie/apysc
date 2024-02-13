import apysc as ap
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings
from tests._material_design.icon.material_icons_common import assert_constructor


class TestMaterialCircleUpIcon:
    @apply_test_settings()
    def test__init__(self) -> None:
        assert_constructor(
            icon_class=ap.MaterialCircleUpIcon,
            expected_variable_name=var_names.MATERIAL_CIRCLE_UP_ICON,
        )
