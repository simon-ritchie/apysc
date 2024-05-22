from apysc._material_design.icon.material_send_outlined_icon import (
    MaterialSendOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSendOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSendOutlinedIcon = MaterialSendOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
