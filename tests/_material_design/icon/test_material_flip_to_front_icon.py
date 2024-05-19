from apysc._material_design.icon.material_flip_to_front_icon import (
    MaterialflipToFrontIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialflipToFrontIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialflipToFrontIcon = MaterialflipToFrontIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
