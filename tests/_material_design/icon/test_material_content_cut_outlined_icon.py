from apysc._material_design.icon.material_content_cut_outlined_icon import MaterialcontentCutOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcontentCutOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcontentCutOutlinedIcon = MaterialcontentCutOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
