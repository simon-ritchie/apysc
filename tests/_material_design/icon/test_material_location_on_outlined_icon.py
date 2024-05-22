from apysc._material_design.icon.material_location_on_outlined_icon import (
    MaterialLocationOnOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialLocationOnOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialLocationOnOutlinedIcon = MaterialLocationOnOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
