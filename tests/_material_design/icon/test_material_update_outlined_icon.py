from apysc._material_design.icon.material_update_outlined_icon import (
    MaterialupdateOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialupdateOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialupdateOutlinedIcon = MaterialupdateOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
