from apysc._material_design.icon.material_thumb_down_off_alt_icon import (
    MaterialthumbDownOffAltIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialthumbDownOffAltIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialthumbDownOffAltIcon = MaterialthumbDownOffAltIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
