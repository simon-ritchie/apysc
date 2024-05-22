from apysc._material_design.icon.material_text_rotation_angledown_icon import (
    MaterialTextRotationAngledownIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialTextRotationAngledownIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialTextRotationAngledownIcon = MaterialTextRotationAngledownIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
