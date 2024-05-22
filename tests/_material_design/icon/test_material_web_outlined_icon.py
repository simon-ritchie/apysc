from apysc._material_design.icon.material_web_outlined_icon import (
    MaterialWebOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialWebOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialWebOutlinedIcon = MaterialWebOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
