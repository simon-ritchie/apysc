from apysc._material_design.icon.material_open_in_full_icon import MaterialopenInFullIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialopenInFullIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialopenInFullIcon = MaterialopenInFullIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
