from apysc._material_design.icon.material_cancel_presentation_icon import (
    MaterialCancelPresentationIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCancelPresentationIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCancelPresentationIcon = MaterialCancelPresentationIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
