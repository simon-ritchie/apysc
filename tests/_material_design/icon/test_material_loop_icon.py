from apysc._material_design.icon.material_loop_icon import MaterialloopIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialloopIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialloopIcon = MaterialloopIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
