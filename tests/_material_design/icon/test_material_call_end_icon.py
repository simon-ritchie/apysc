from apysc._material_design.icon.material_call_end_icon import MaterialcallEndIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcallEndIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcallEndIcon = MaterialcallEndIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
