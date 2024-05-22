from apysc._material_design.icon.material_remove_circle_outline_icon import (
    MaterialRemoveCircleOutlineIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialRemoveCircleOutlineIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialRemoveCircleOutlineIcon = MaterialRemoveCircleOutlineIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
