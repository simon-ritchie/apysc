from apysc._material_design.icon.material_preview_icon import MaterialpreviewIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialpreviewIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialpreviewIcon = MaterialpreviewIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
