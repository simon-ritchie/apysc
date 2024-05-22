from apysc._material_design.icon.material_outbond_outlined_icon import (
    MaterialOutbondOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialOutbondOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialOutbondOutlinedIcon = MaterialOutbondOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
