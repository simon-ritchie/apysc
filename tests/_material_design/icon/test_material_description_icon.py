from apysc._material_design.icon.material_description_icon import (
    MaterialDescriptionIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialDescriptionIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialDescriptionIcon = MaterialDescriptionIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
