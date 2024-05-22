from apysc._material_design.icon.material_location_off_outlined_icon import (
    MaterialLocationOffOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialLocationOffOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialLocationOffOutlinedIcon = MaterialLocationOffOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
