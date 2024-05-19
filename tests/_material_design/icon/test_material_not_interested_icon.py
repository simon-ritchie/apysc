from apysc._material_design.icon.material_not_interested_icon import MaterialnotInterestedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialnotInterestedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialnotInterestedIcon = MaterialnotInterestedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
