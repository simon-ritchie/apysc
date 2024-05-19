from apysc._material_design.icon.material_web_asset_outlined_icon import (
    MaterialwebAssetOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialwebAssetOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialwebAssetOutlinedIcon = MaterialwebAssetOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
