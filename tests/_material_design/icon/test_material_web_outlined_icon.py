from apysc._material_design.icon.material_web_outlined_icon import (
    MaterialwebOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialwebOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialwebOutlinedIcon = MaterialwebOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
