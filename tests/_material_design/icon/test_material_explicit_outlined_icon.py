from apysc._material_design.icon.material_explicit_outlined_icon import (
    MaterialExplicitOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialExplicitOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialExplicitOutlinedIcon = MaterialExplicitOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
