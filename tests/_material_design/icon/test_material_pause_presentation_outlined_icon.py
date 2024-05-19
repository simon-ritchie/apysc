from apysc._material_design.icon.material_pause_presentation_outlined_icon import MaterialpausePresentationOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialpausePresentationOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialpausePresentationOutlinedIcon = MaterialpausePresentationOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
