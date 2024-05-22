from apysc._material_design.icon.material_account_box_outlined_icon import (
    MaterialAccountBoxOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAccountBoxOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAccountBoxOutlinedIcon = MaterialAccountBoxOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
