from apysc._material_design.icon.material_present_to_all_outlined_icon import (
    MaterialPresentToAllOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPresentToAllOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPresentToAllOutlinedIcon = MaterialPresentToAllOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
