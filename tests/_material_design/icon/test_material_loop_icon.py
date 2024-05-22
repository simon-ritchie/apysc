from apysc._material_design.icon.material_loop_icon import MaterialLoopIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialLoopIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialLoopIcon = MaterialLoopIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
