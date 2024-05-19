from apysc._material_design.icon.material_content_cut_icon import MaterialcontentCutIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcontentCutIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcontentCutIcon = MaterialcontentCutIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
