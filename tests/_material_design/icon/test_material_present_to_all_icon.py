from apysc._material_design.icon.material_present_to_all_icon import (
    MaterialPresentToAllIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPresentToAllIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPresentToAllIcon = MaterialPresentToAllIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
