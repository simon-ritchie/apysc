from apysc._material_design.icon.material_clear_outlined_icon import (
    MaterialClearOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialClearOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialClearOutlinedIcon = MaterialClearOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
