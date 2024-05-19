from apysc._material_design.icon.material_eject_icon import MaterialejectIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialejectIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialejectIcon = MaterialejectIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
