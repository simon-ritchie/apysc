from apysc._material_design.icon.material_speaker_notes_off_outlined_icon import (
    MaterialSpeakerNotesOffOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSpeakerNotesOffOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSpeakerNotesOffOutlinedIcon = (
            MaterialSpeakerNotesOffOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
