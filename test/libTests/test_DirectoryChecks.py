import os

import pytest

from lib.DirectoryChecks import is_there_entered_value_that_is_directory


class TestDirectoryChecks:

    @pytest.mark.regression
    @pytest.mark.parametrize("directory, isdir, expected", [
        ("", True, True),
        ("", False, True),
        ("Fake", True, True),
        ("Fake", False, False)
    ])
    def test_is_there_entered_value_that_is_directory(self, directory, isdir, expected, monkeypatch):
        monkeypatch.setattr(os.path, "isdir", lambda x: isdir)

        assert is_there_entered_value_that_is_directory(directory) == expected
