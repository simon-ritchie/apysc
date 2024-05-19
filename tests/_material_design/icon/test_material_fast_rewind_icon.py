from apysc._material_design.icon.material_fast_rewind_icon import MaterialfastRewindIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialfastRewindIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialfastRewindIcon = MaterialfastRewindIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
