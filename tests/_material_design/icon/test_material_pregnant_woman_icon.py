from apysc._material_design.icon.material_pregnant_woman_icon import (
    MaterialpregnantWomanIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialpregnantWomanIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialpregnantWomanIcon = MaterialpregnantWomanIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
