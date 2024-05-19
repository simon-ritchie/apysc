from apysc._material_design.icon.material_speaker_notes_outlined_icon import MaterialspeakerNotesOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialspeakerNotesOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialspeakerNotesOutlinedIcon = MaterialspeakerNotesOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
