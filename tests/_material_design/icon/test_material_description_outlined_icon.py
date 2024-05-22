from apysc._material_design.icon.material_description_outlined_icon import (
    MaterialDescriptionOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialDescriptionOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialDescriptionOutlinedIcon = MaterialDescriptionOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
