from apysc._material_design.icon.material_web_asset_icon import MaterialwebAssetIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialwebAssetIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialwebAssetIcon = MaterialwebAssetIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
