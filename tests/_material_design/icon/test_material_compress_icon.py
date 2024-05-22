from apysc._material_design.icon.material_compress_icon import MaterialCompressIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCompressIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCompressIcon = MaterialCompressIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
