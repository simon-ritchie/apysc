from apysc._material_design.icon.material_gif_icon import MaterialgifIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialgifIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialgifIcon = MaterialgifIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
