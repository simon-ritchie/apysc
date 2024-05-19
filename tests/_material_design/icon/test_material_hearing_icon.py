from apysc._material_design.icon.material_hearing_icon import MaterialhearingIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialhearingIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialhearingIcon = MaterialhearingIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
