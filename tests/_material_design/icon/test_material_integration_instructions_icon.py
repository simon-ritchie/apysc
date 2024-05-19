from apysc._material_design.icon.material_integration_instructions_icon import (
    MaterialintegrationInstructionsIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialintegrationInstructionsIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialintegrationInstructionsIcon = (
            MaterialintegrationInstructionsIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
