import pytest

from libs.ParseExtensions import parse_extensions


class TestParseExtensions:

    @pytest.mark.regression
    @pytest.mark.parametrize("extensions, expected", [
        ("php", (".php",)),
        ("php, .hop .BIB BOP, Lim", (".php", ".hop", ".bib", ".bop", ".lim")),
        ("", ("",))
    ])
    def test_entered_extensions__parsed_into_lowercase_tuple(self, extensions, expected):
        assert parse_extensions(extensions) == expected
