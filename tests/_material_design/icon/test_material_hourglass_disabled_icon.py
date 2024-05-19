from apysc._material_design.icon.material_hourglass_disabled_icon import (
    MaterialhourglassDisabledIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialhourglassDisabledIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialhourglassDisabledIcon = MaterialhourglassDisabledIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
