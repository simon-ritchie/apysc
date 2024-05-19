from apysc._material_design.icon.material_list_outlined_icon import (
    MateriallistOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMateriallistOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MateriallistOutlinedIcon = MateriallistOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
