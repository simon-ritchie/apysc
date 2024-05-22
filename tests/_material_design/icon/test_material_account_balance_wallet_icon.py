from apysc._material_design.icon.material_account_balance_wallet_icon import (
    MaterialAccountBalanceWalletIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAccountBalanceWalletIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAccountBalanceWalletIcon = MaterialAccountBalanceWalletIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
