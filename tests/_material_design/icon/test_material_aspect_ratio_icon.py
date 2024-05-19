from apysc._material_design.icon.material_aspect_ratio_icon import (
    MaterialaspectRatioIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialaspectRatioIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialaspectRatioIcon = MaterialaspectRatioIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
