from apysc._material_design.icon.material_build_circle_icon import (
    MaterialBuildCircleIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialBuildCircleIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialBuildCircleIcon = MaterialBuildCircleIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
