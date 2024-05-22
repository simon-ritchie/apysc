from apysc._material_design.icon.material_supervised_user_circle_icon import (
    MaterialSupervisedUserCircleIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSupervisedUserCircleIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSupervisedUserCircleIcon = MaterialSupervisedUserCircleIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
