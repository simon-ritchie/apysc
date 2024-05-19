from apysc._material_design.icon.material_rowing_icon import MaterialrowingIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialrowingIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialrowingIcon = MaterialrowingIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
