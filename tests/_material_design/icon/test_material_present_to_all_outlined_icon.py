from apysc._material_design.icon.material_present_to_all_outlined_icon import (
    MaterialpresentToAllOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialpresentToAllOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialpresentToAllOutlinedIcon = MaterialpresentToAllOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
