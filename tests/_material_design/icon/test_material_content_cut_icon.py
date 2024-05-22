from apysc._material_design.icon.material_content_cut_icon import MaterialContentCutIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialContentCutIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialContentCutIcon = MaterialContentCutIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
