from apysc._material_design.icon.material_markunread_icon import MaterialMarkunreadIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialMarkunreadIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialMarkunreadIcon = MaterialMarkunreadIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
