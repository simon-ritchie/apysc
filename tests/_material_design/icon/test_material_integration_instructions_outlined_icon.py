from apysc._material_design.icon.material_integration_instructions_outlined_icon import (  # noqa
    MaterialIntegrationInstructionsOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialIntegrationInstructionsOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialIntegrationInstructionsOutlinedIcon = (
            MaterialIntegrationInstructionsOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
