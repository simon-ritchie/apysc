from apysc._material_design.icon.material_aspect_ratio_outlined_icon import (
    MaterialAspectRatioOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAspectRatioOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAspectRatioOutlinedIcon = MaterialAspectRatioOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
