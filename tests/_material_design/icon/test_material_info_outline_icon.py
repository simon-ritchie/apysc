from apysc._material_design.icon.material_info_outline_icon import (
    MaterialInfoOutlineIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialInfoOutlineIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialInfoOutlineIcon = MaterialInfoOutlineIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
