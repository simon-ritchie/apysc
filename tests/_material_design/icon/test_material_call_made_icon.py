from apysc._material_design.icon.material_call_made_icon import MaterialCallMadeIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCallMadeIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCallMadeIcon = MaterialCallMadeIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
