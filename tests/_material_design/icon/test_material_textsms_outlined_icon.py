from apysc._material_design.icon.material_textsms_outlined_icon import (
    MaterialtextsmsOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialtextsmsOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialtextsmsOutlinedIcon = MaterialtextsmsOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
