from apysc._material_design.icon.material_contactless_outlined_icon import (
    MaterialcontactlessOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcontactlessOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcontactlessOutlinedIcon = MaterialcontactlessOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
