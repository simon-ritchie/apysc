from apysc._material_design.icon.material_textsms_icon import MaterialtextsmsIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialtextsmsIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialtextsmsIcon = MaterialtextsmsIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
