from apysc._material_design.icon.material_movie_icon import MaterialMovieIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialMovieIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialMovieIcon = MaterialMovieIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
