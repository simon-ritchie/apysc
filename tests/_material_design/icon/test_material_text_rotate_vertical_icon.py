from apysc._material_design.icon.material_text_rotate_vertical_icon import MaterialtextRotateVerticalIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialtextRotateVerticalIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialtextRotateVerticalIcon = MaterialtextRotateVerticalIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
