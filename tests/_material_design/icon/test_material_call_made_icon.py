from apysc._material_design.icon.material_call_made_icon import MaterialcallMadeIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcallMadeIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcallMadeIcon = MaterialcallMadeIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
