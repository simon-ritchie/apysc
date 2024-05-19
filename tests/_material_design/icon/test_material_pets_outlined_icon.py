from apysc._material_design.icon.material_pets_outlined_icon import (
    MaterialpetsOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialpetsOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialpetsOutlinedIcon = MaterialpetsOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
