from apysc._material_design.icon.material_supervised_user_circle_outlined_icon import MaterialsupervisedUserCircleOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialsupervisedUserCircleOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialsupervisedUserCircleOutlinedIcon = MaterialsupervisedUserCircleOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
