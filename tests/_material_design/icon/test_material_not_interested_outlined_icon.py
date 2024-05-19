from apysc._material_design.icon.material_not_interested_outlined_icon import MaterialnotInterestedOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialnotInterestedOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialnotInterestedOutlinedIcon = MaterialnotInterestedOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
