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

        num_files = 0
        for file in get_files("root"):
            num_files += 1

        assert num_files == 11

    @pytest.mark.regression
    @pytest.mark.parametrize("type_filter, expected", [
        ((".hhp",), ["/Fake/bop.HHP", "/Fake/bar/blip/bop/hop.hhp"]),
        ((".hhp", ".qrz"), ["/Fake/bop.HHP", "/Fake/bar/blip/bop/hop.hhp", "/Fake/boo/pil.qrz"]),
        (("kozyer",), [])
    ])
    def test_if_file_type_filter__return_all_files_of_type_regardless_of_case(self, type_filter, expected, monkeypatch):
        monkeypatch.setattr(os.path, "isdir", lambda x: True)
        monkeypatch.setattr(os, "walk", self._walk_fake)

        for src, name in get_files("fake", type_filter):
            expected.remove(os.path.join(src, name))
        assert len(expected) == 0

    @pytest.mark.regression
    def test_if_file_type_filter__files_without_extensions_not_returned(self, monkeypatch):
        expected = ["/Fake/goo.ppk", "/Fake/boo/qui.ppk", "/Fake/bar/blip/gim.ppk"]
        monkeypatch.setattr(os.path, "isdir", lambda x: True)
        monkeypatch.setattr(os, "walk", self._walk_fake)

        for src, name in get_files("fake", (".ppk",)):
            expected.remove(os.path.join(src, name))
        assert len(expected) == 0

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
