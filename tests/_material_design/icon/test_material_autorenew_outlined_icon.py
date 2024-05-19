from apysc._material_design.icon.material_autorenew_outlined_icon import (
    MaterialautorenewOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialautorenewOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialautorenewOutlinedIcon = MaterialautorenewOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
