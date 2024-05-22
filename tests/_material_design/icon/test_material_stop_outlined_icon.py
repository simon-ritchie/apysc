from apysc._material_design.icon.material_stop_outlined_icon import (
    MaterialStopOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialStopOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialStopOutlinedIcon = MaterialStopOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
