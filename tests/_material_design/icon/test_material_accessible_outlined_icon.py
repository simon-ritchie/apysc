from apysc._material_design.icon.material_accessible_outlined_icon import (
    MaterialAccessibleOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAccessibleOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAccessibleOutlinedIcon = MaterialAccessibleOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
