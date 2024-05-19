from apysc._material_design.icon.material_rounded_corner_icon import (
    MaterialroundedCornerIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialroundedCornerIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialroundedCornerIcon = MaterialroundedCornerIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
