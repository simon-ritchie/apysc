from apysc._material_design.icon.material_speaker_notes_off_icon import (
    MaterialSpeakerNotesOffIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSpeakerNotesOffIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSpeakerNotesOffIcon = MaterialSpeakerNotesOffIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
