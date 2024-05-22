from apysc._material_design.icon.material_markunread_outlined_icon import (
    MaterialMarkunreadOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialMarkunreadOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialMarkunreadOutlinedIcon = MaterialMarkunreadOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
