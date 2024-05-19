from apysc._material_design.icon.material_compress_icon import MaterialcompressIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcompressIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcompressIcon = MaterialcompressIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
