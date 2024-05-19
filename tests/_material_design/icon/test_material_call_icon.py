from apysc._material_design.icon.material_call_icon import MaterialcallIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcallIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcallIcon = MaterialcallIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
