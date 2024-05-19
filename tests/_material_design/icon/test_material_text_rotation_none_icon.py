from apysc._material_design.icon.material_text_rotation_none_icon import (
    MaterialtextRotationNoneIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialtextRotationNoneIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialtextRotationNoneIcon = MaterialtextRotationNoneIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
