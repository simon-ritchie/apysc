from apysc._material_design.icon.material_repeat_outlined_icon import (
    MaterialRepeatOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialRepeatOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialRepeatOutlinedIcon = MaterialRepeatOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
