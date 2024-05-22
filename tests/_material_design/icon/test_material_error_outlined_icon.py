from apysc._material_design.icon.material_error_outlined_icon import (
    MaterialErrorOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialErrorOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialErrorOutlinedIcon = MaterialErrorOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
