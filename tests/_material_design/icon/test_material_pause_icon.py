from apysc._material_design.icon.material_pause_icon import MaterialpauseIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialpauseIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialpauseIcon = MaterialpauseIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
