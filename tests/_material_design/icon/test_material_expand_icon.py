from apysc._material_design.icon.material_expand_icon import MaterialExpandIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialExpandIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialExpandIcon = MaterialExpandIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
