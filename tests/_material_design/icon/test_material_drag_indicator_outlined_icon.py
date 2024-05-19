from apysc._material_design.icon.material_drag_indicator_outlined_icon import (
    MaterialdragIndicatorOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialdragIndicatorOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialdragIndicatorOutlinedIcon = MaterialdragIndicatorOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
