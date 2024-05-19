from apysc._material_design.icon.material_person_add_disabled_outlined_icon import (
    MaterialpersonAddDisabledOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialpersonAddDisabledOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialpersonAddDisabledOutlinedIcon = (
            MaterialpersonAddDisabledOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
