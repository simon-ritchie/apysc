from apysc._material_design.icon.material_speaker_notes_outlined_icon import (
    MaterialSpeakerNotesOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSpeakerNotesOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSpeakerNotesOutlinedIcon = MaterialSpeakerNotesOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
