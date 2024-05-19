from apysc._material_design.icon.material_call_made_outlined_icon import (
    MaterialcallMadeOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcallMadeOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcallMadeOutlinedIcon = MaterialcallMadeOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
