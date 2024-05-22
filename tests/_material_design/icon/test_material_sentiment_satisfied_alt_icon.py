from apysc._material_design.icon.material_sentiment_satisfied_alt_icon import (
    MaterialSentimentSatisfiedAltIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSentimentSatisfiedAltIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSentimentSatisfiedAltIcon = MaterialSentimentSatisfiedAltIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
