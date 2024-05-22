from apysc._material_design.icon.material_exit_to_app_outlined_icon import (
    MaterialExitToAppOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialExitToAppOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialExitToAppOutlinedIcon = MaterialExitToAppOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
