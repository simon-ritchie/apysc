from apysc._material_design.icon.material_speaker_notes_off_outlined_icon import (
    MaterialspeakerNotesOffOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialspeakerNotesOffOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialspeakerNotesOffOutlinedIcon = (
            MaterialspeakerNotesOffOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
