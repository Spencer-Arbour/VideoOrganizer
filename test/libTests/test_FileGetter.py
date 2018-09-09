import os

import pytest

from lib.FileGetter import get_files


class TestFileGetter:

    @pytest.mark.regression
    def test_root_directory_does_not_exit__throw_not_directory_error(self, monkeypatch):
        monkeypatch.setattr(os.path, "isdir", lambda x: False)

        with pytest.raises(NotADirectoryError) as ex_info:
            get_files("fake")

        assert str(ex_info.value) == "Dir does not exist"

    @pytest.mark.regression
    def test_if_no_filter__return_all_files(self, monkeypatch):
        monkeypatch.setattr(os.path, "isdir", lambda x: True)
        monkeypatch.setattr(os, "walk", self._walk_fake)

        file_list = get_files("fake", ("",))
        assert len(file_list) == 5

    @pytest.mark.regression
    @pytest.mark.parametrize("type_filter, expected", [
        ((".hhp",), {"/Fake": {"bop.HHP"}, "/Fake/bar/blip/bop": {"hop.hhp"}}),
        ((".hhp", ".qrz"), {"/Fake": {"bop.HHP"}, "/Fake/bar/blip/bop": {"hop.hhp"}, "/Fake/boo": {"pil.qrz"}}),
        (("kozyer",), {})
    ])
    def test_if_file_type_filter__return_all_files_of_type_regardless_of_case(self, type_filter, expected, monkeypatch):
        monkeypatch.setattr(os.path, "isdir", lambda x: True)
        monkeypatch.setattr(os, "walk", self._walk_fake)

        files = get_files("fake", type_filter)

        assert files.keys() == expected.keys()
        for key, values in expected.items():
            assert values == files[key]

    @pytest.mark.regression
    def test_if_file_type_filter__files_without_extensions_not_returned(self, monkeypatch):
        expected = {"/Fake": {"goo.ppk"}, "/Fake/boo": {"qui.ppk"}, "/Fake/bar/blip": {"gim.ppk"}}
        monkeypatch.setattr(os.path, "isdir", lambda x: True)
        monkeypatch.setattr(os, "walk", self._walk_fake)

        files = get_files("fake", (".ppk",))

        assert files.keys() == expected.keys()
        for key, values in expected.items():
            assert values == files[key]

    # noinspection PyUnusedLocal
    @staticmethod
    def _walk_fake(top):
        return [
            ("/Fake", ["boo", "bar", "biz"], ["bop.HHP", "goo.ppk"]),
            ("/Fake/boo", [], ["pil.qrz", "qui.ppk"]),
            ("/Fake/bar", ["blip"], []),
            ("/Fake/bar/blip", ["bop"], ["kapa.bin", "gim.ppk"]),
            ("/Fake/bar/blip/bop", [], ["car.hum", "lip.pil", "hah.aha", "hop.hhp"]),
            ("/Fake/biz", [], ["fileppk"])]
