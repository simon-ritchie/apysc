from apysc._material_design.icon.material_perm_identity_icon import (
    MaterialpermIdentityIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialpermIdentityIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialpermIdentityIcon = MaterialpermIdentityIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
