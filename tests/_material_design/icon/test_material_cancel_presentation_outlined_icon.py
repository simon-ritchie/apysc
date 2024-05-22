from apysc._material_design.icon.material_cancel_presentation_outlined_icon import (
    MaterialCancelPresentationOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCancelPresentationOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCancelPresentationOutlinedIcon = (
            MaterialCancelPresentationOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
