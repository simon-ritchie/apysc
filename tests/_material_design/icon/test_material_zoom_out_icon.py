from apysc._material_design.icon.material_zoom_out_icon import MaterialzoomOutIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialzoomOutIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialzoomOutIcon = MaterialzoomOutIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
