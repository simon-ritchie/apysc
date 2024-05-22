from apysc._material_design.icon.material_text_rotate_vertical_icon import (
    MaterialTextRotateVerticalIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialTextRotateVerticalIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialTextRotateVerticalIcon = MaterialTextRotateVerticalIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
