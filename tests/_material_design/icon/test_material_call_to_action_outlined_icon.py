from apysc._material_design.icon.material_call_to_action_outlined_icon import (
    MaterialcallToActionOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcallToActionOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcallToActionOutlinedIcon = MaterialcallToActionOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
