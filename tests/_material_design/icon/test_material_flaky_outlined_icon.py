from apysc._material_design.icon.material_flaky_outlined_icon import (
    MaterialflakyOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialflakyOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialflakyOutlinedIcon = MaterialflakyOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
