from apysc._material_design.icon.material_content_copy_icon import MaterialcontentCopyIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcontentCopyIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcontentCopyIcon = MaterialcontentCopyIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
