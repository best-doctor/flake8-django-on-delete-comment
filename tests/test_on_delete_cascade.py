from conftest import run_validator_for_test_files


def test_on_delete_cascade_with_noqa():
    errors = run_validator_for_test_files('on_delete_cascade_with_noqa.py')
    assert len(errors) == 0


def test_on_delete_cascade_without_noqa():
    errors = run_validator_for_test_files('on_delete_cascade_without_noqa.py')
    assert len(errors) == 1
