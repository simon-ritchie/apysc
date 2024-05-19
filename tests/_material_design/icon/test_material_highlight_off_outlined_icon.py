from apysc._material_design.icon.material_highlight_off_outlined_icon import (
    MaterialhighlightOffOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialhighlightOffOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialhighlightOffOutlinedIcon = MaterialhighlightOffOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
