from apysc._material_design.icon.material_perm_identity_outlined_icon import MaterialpermIdentityOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialpermIdentityOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialpermIdentityOutlinedIcon = MaterialpermIdentityOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
