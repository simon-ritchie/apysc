from apysc._material_design.icon.material_remove_circle_outlined_icon import (
    MaterialRemoveCircleOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialRemoveCircleOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialRemoveCircleOutlinedIcon = MaterialRemoveCircleOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
