from apysc._material_design.icon.material_text_rotate_up_icon import MaterialtextRotateUpIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialtextRotateUpIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialtextRotateUpIcon = MaterialtextRotateUpIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
