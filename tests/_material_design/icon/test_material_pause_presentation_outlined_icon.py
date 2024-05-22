from apysc._material_design.icon.material_pause_presentation_outlined_icon import (
    MaterialPausePresentationOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPausePresentationOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPausePresentationOutlinedIcon = (
            MaterialPausePresentationOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
