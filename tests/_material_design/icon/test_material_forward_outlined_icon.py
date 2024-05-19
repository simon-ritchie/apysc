from apysc._material_design.icon.material_forward_outlined_icon import (
    MaterialforwardOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialforwardOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialforwardOutlinedIcon = MaterialforwardOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
