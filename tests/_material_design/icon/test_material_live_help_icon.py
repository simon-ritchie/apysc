from apysc._material_design.icon.material_live_help_icon import MaterialLiveHelpIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialLiveHelpIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialLiveHelpIcon = MaterialLiveHelpIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
