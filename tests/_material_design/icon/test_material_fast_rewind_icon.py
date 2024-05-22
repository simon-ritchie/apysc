from apysc._material_design.icon.material_fast_rewind_icon import MaterialFastRewindIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialFastRewindIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialFastRewindIcon = MaterialFastRewindIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
