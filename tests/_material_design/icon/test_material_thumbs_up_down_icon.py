from apysc._material_design.icon.material_thumbs_up_down_icon import MaterialthumbsUpDownIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialthumbsUpDownIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialthumbsUpDownIcon = MaterialthumbsUpDownIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
