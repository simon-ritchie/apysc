from apysc._material_design.icon.material_api_outlined_icon import MaterialapiOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialapiOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialapiOutlinedIcon = MaterialapiOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
