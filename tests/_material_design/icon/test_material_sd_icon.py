from apysc._material_design.icon.material_sd_icon import MaterialSdIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSdIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSdIcon = MaterialSdIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
