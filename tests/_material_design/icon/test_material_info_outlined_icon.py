from apysc._material_design.icon.material_info_outlined_icon import (
    MaterialInfoOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialInfoOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialInfoOutlinedIcon = MaterialInfoOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
