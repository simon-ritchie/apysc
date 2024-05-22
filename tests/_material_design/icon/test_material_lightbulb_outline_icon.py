from apysc._material_design.icon.material_lightbulb_outline_icon import (
    MaterialLightbulbOutlineIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialLightbulbOutlineIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialLightbulbOutlineIcon = MaterialLightbulbOutlineIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
