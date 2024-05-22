from apysc._material_design.icon.material_stop_icon import MaterialStopIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialStopIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialStopIcon = MaterialStopIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
