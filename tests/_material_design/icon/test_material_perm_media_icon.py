from apysc._material_design.icon.material_perm_media_icon import MaterialpermMediaIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialpermMediaIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialpermMediaIcon = MaterialpermMediaIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
