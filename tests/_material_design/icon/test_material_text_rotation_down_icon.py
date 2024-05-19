from apysc._material_design.icon.material_text_rotation_down_icon import MaterialtextRotationDownIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialtextRotationDownIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialtextRotationDownIcon = MaterialtextRotationDownIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
