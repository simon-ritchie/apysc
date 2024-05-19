from apysc._material_design.icon.material_stars_icon import MaterialstarsIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialstarsIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialstarsIcon = MaterialstarsIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
