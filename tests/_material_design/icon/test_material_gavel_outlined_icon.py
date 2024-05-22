from apysc._material_design.icon.material_gavel_outlined_icon import (
    MaterialGavelOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialGavelOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialGavelOutlinedIcon = MaterialGavelOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
