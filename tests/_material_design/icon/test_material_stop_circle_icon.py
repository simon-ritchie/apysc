from apysc._material_design.icon.material_stop_circle_icon import MaterialstopCircleIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialstopCircleIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialstopCircleIcon = MaterialstopCircleIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
