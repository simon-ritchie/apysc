from apysc._material_design.icon.material_location_on_icon import MaterialLocationOnIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialLocationOnIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialLocationOnIcon = MaterialLocationOnIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
