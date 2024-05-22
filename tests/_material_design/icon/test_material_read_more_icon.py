from apysc._material_design.icon.material_read_more_icon import MaterialReadMoreIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialReadMoreIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialReadMoreIcon = MaterialReadMoreIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
