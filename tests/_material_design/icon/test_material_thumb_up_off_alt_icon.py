from apysc._material_design.icon.material_thumb_up_off_alt_icon import (
    MaterialthumbUpOffAltIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialthumbUpOffAltIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialthumbUpOffAltIcon = MaterialthumbUpOffAltIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
