from apysc._material_design.icon.material_aspect_ratio_icon import (
    MaterialAspectRatioIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAspectRatioIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAspectRatioIcon = MaterialAspectRatioIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
