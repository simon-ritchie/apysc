from apysc._material_design.icon.material_view_quilt_outlined_icon import (
    MaterialviewQuiltOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialviewQuiltOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialviewQuiltOutlinedIcon = MaterialviewQuiltOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
