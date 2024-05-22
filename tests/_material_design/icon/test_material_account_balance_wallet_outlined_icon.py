from apysc._material_design.icon.material_account_balance_wallet_outlined_icon import (
    MaterialAccountBalanceWalletOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAccountBalanceWalletOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAccountBalanceWalletOutlinedIcon = (
            MaterialAccountBalanceWalletOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
