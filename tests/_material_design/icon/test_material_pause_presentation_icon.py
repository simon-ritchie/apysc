from apysc._material_design.icon.material_pause_presentation_icon import (
    MaterialPausePresentationIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPausePresentationIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPausePresentationIcon = MaterialPausePresentationIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
