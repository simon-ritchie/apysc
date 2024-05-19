from apysc._material_design.icon.material_account_box_outlined_icon import (
    MaterialaccountBoxOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialaccountBoxOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialaccountBoxOutlinedIcon = MaterialaccountBoxOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
