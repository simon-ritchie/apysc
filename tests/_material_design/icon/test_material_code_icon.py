from apysc._material_design.icon.material_code_icon import MaterialCodeIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCodeIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCodeIcon = MaterialCodeIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
