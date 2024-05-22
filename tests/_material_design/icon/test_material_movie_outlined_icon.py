from apysc._material_design.icon.material_movie_outlined_icon import (
    MaterialMovieOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialMovieOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialMovieOutlinedIcon = MaterialMovieOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
