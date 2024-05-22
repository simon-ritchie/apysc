from apysc._material_design.icon.material_copyright_icon import MaterialCopyrightIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCopyrightIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCopyrightIcon = MaterialCopyrightIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
