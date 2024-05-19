from apysc._material_design.icon.material_outlined_flag_icon import MaterialoutlinedFlagIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialoutlinedFlagIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialoutlinedFlagIcon = MaterialoutlinedFlagIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
