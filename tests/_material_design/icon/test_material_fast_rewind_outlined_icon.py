from apysc._material_design.icon.material_fast_rewind_outlined_icon import MaterialfastRewindOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialfastRewindOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialfastRewindOutlinedIcon = MaterialfastRewindOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
