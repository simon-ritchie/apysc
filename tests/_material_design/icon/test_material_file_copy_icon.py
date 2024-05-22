from apysc._material_design.icon.material_file_copy_icon import MaterialFileCopyIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialFileCopyIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialFileCopyIcon = MaterialFileCopyIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
