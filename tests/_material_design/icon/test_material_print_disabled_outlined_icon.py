from apysc._material_design.icon.material_print_disabled_outlined_icon import MaterialprintDisabledOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialprintDisabledOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialprintDisabledOutlinedIcon = MaterialprintDisabledOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
