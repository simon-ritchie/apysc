from apysc._material_design.icon.material_perm_identity_icon import (
    MaterialPermIdentityIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPermIdentityIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPermIdentityIcon = MaterialPermIdentityIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
