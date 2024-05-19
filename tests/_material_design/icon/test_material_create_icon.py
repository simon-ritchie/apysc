from apysc._material_design.icon.material_create_icon import MaterialcreateIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcreateIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcreateIcon = MaterialcreateIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
