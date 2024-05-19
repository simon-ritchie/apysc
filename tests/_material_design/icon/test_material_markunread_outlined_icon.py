from apysc._material_design.icon.material_markunread_outlined_icon import (
    MaterialmarkunreadOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialmarkunreadOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialmarkunreadOutlinedIcon = MaterialmarkunreadOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
