from apysc._material_design.icon.material_stars_outlined_icon import (
    MaterialstarsOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialstarsOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialstarsOutlinedIcon = MaterialstarsOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
