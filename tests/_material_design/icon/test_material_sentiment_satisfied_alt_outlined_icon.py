from apysc._material_design.icon.material_sentiment_satisfied_alt_outlined_icon import (
    MaterialSentimentSatisfiedAltOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSentimentSatisfiedAltOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSentimentSatisfiedAltOutlinedIcon = (
            MaterialSentimentSatisfiedAltOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
