from apysc._material_design.icon.material_flag_icon import MaterialflagIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialflagIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialflagIcon = MaterialflagIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
