from apysc._material_design.icon.material_flip_to_front_outlined_icon import (
    MaterialflipToFrontOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialflipToFrontOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialflipToFrontOutlinedIcon = MaterialflipToFrontOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
