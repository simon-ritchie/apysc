from apysc._material_design.icon.material_perm_media_icon import MaterialPermMediaIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPermMediaIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPermMediaIcon = MaterialPermMediaIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
