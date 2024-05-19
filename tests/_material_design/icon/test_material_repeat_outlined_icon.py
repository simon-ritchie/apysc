from apysc._material_design.icon.material_repeat_outlined_icon import (
    MaterialrepeatOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialrepeatOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialrepeatOutlinedIcon = MaterialrepeatOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
