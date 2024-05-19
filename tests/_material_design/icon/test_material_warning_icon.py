from apysc._material_design.icon.material_warning_icon import MaterialwarningIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialwarningIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialwarningIcon = MaterialwarningIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
