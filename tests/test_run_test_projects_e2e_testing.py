from random import randint
from typing import List

from retrying import retry

from scripts import run_test_projects_e2e_testing


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_target_test_project_main_module_paths() -> None:
    main_module_paths: List[str] = run_test_projects_e2e_testing.\
        _get_target_test_project_main_module_paths(
            alphabets_group=['a', 'b'])
    expected_paths: List[str] = [
        './test_projects/AnimationXInterface/main.py',
        './test_projects/Boolean/main.py',
    ]
    for expected_path in expected_paths:
        assert expected_path in main_module_paths

    unexpected_paths: List[str] = [
        './test_projects/ClickInterface/main.py',
    ]
    for unexpected_path in unexpected_paths:
        assert unexpected_path not in main_module_paths
