from apysc._material_design.icon.material_speaker_notes_icon import (
    MaterialSpeakerNotesIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSpeakerNotesIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSpeakerNotesIcon = MaterialSpeakerNotesIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
