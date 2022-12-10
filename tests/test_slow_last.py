"""Testing the pytest-nice plugin."""

import pytest


@pytest.fixture()
def sample_test(testdir):
    testdir.makepyfile(
        """
        from time import sleep
        def test_pass():
            sleep(0.15)
            assert 1 == 1

        def test_fail():
            sleep(0.01)
            assert 1 == 2
    """
    )
    return testdir


def test_without_slow(sample_test):
    result = sample_test.runpytest()
    result.stdout.fnmatch_lines(
        [
            "*.F*",
        ]
    )  # . for Pass, F for Fail
    assert result.ret == 1


def test_with_slow(sample_test):
    sample_test.runpytest("")
    result = sample_test.runpytest("--slow-last")
    result.stdout.fnmatch_lines(
        [
            "*F.*",
        ]
    )  # . for Pass, F for Fail
    assert result.ret == 1


def test_ff_preference(sample_test):
    sample_test.runpytest("")
    result = sample_test.runpytest("--slow-last", "--ff")
    result.stdout.fnmatch_lines(
        [
            "*F.*",
        ]
    )  # . for Pass, F for Fail
    assert result.ret == 1


def test_help_message(testdir):
    result = testdir.runpytest(
        "--help",
    )
    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines(
        [
            "*Run slowest tests last*",
        ]
    )


def test_hello_ini_setting(testdir):
    testdir.makeini(
        """
        [pytest]
        addopts = --slow-last
    """
    )

    testdir.makepyfile(
        """
        from time import sleep
        def test_slow():
            sleep(0.15)

        def test_fast():
            sleep(0.01)
    """
    )

    testdir.runpytest("")
    result = testdir.runpytest("-v")

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines(
        [
            "*::test_fast PASSED*",
            "*::test_slow PASSED*",
        ]
    )

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0
