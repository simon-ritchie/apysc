from apysc._material_design.icon.material_account_balance_outlined_icon import (
    MaterialAccountBalanceOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAccountBalanceOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAccountBalanceOutlinedIcon = MaterialAccountBalanceOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
