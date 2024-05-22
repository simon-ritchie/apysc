from apysc._material_design.icon.material_fast_forward_outlined_icon import (
    MaterialFastForwardOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialFastForwardOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialFastForwardOutlinedIcon = MaterialFastForwardOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
