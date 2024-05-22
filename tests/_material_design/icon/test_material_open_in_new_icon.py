from apysc._material_design.icon.material_open_in_new_icon import MaterialOpenInNewIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialOpenInNewIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialOpenInNewIcon = MaterialOpenInNewIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
