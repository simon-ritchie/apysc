from apysc._material_design.icon.material_airplay_outlined_icon import (
    MaterialAirplayOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAirplayOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAirplayOutlinedIcon = MaterialAirplayOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
