from apysc._material_design.icon.material_http_outlined_icon import (
    MaterialHttpOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialHttpOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialHttpOutlinedIcon = MaterialHttpOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
