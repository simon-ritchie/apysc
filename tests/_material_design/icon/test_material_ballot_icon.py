from apysc._material_design.icon.material_ballot_icon import MaterialBallotIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialBallotIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialBallotIcon = MaterialBallotIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
