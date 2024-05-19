from apysc._material_design.icon.material_description_icon import (
    MaterialdescriptionIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialdescriptionIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialdescriptionIcon = MaterialdescriptionIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
