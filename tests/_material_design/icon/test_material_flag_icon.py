from apysc._material_design.icon.material_flag_icon import MaterialFlagIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialFlagIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialFlagIcon = MaterialFlagIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
