from apysc._material_design.icon.material_textsms_icon import MaterialTextsmsIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialTextsmsIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialTextsmsIcon = MaterialTextsmsIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
