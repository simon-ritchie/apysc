from apysc._material_design.icon.material_pets_outlined_icon import (
    MaterialPetsOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPetsOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPetsOutlinedIcon = MaterialPetsOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
