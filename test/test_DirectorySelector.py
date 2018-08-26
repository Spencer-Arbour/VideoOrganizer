from tkinter import messagebox, Entry, filedialog
from gui.DirectorySelector import DirectorySelector
import pytest
import os


class TestDirectorySelector:

    _DIR_UNDER_TEST = "fooBar"

    @pytest.mark.regression
    @pytest.mark.parametrize("initial_dir, new_dir, ask_dir_calls, delete_insert_calls", [
        (False, "Fake", 0, 0),
        ("foo", "Fake", 1, 1),
        ("foo", "", 1, 0)
    ])
    def test_was_directory_field_changed(self, initial_dir, new_dir, ask_dir_calls, delete_insert_calls, monkeypatch):
        monkeypatch.setattr(DirectorySelector, "_get_valid_initial_dir", lambda x: initial_dir)

        dir_asker_mock = DirAskerMock(initial_dir, new_dir)
        monkeypatch.setattr(filedialog, "askdirectory", dir_asker_mock.ask_directory)

        fake_entry = EntryFake("")
        DirectorySelector.get_directory(fake_entry)

        assert dir_asker_mock.ask_calls == ask_dir_calls
        assert fake_entry.get_calls == 1
        assert fake_entry.insert_calls == delete_insert_calls
        assert fake_entry.delete_calls == delete_insert_calls

    @pytest.mark.regression
    def test_get_valid_initial_dir__no_directory(self):
        assert DirectorySelector._get_valid_initial_dir("") == os.getcwd()

    @pytest.mark.regression
    def test_get_valid_initial_dir__valid_dir(self, monkeypatch):
        fake_dir = "fake"
        monkeypatch.setattr(os.path, "isdir", lambda x: True)
        assert DirectorySelector._get_valid_initial_dir(fake_dir) == fake_dir

    @pytest.mark.regression
    @pytest.mark.parametrize("ask_okay_cancel, initial_dir", [(True, "/"), (False, False)])
    def test_get_valid_initial_dir__ask_okay_cancel(self, ask_okay_cancel, initial_dir, monkeypatch):
        fake_dir = "fake"

        monkeypatch.setattr(os.path, "isdir", lambda x: False)
        mock_ask = AskOkCancelMock(ask_okay_cancel)
        monkeypatch.setattr(messagebox, "askokcancel", mock_ask.ask_ok_cancel)

        assert DirectorySelector._get_valid_initial_dir(fake_dir) == initial_dir
        assert mock_ask.ask_calls == 1


class DirAskerMock:

    def __init__(self, initial_dir, new_dir):
        self._initial_dir = initial_dir
        self._new_dir = new_dir
        self._ask_calls = 0

    @property
    def ask_calls(self):
        return self._ask_calls

    def ask_directory(self, initialdir: str) -> str:
        self._ask_calls += 1
        assert initialdir == self._initial_dir
        return self._new_dir


class AskOkCancelMock:

    def __init__(self, response: bool):
        self._response = response
        self._ask_calls = 0

    @property
    def ask_calls(self) -> int:
        return self._ask_calls

    # noinspection PyUnusedLocal
    def ask_ok_cancel(self, x: str, y: str) -> bool:
        self._ask_calls += 1
        return self._response



class EntryFake(Entry):

    def __init__(self, content, **kw):
        super().__init__(**kw)
        self._content = content

        self._get_calls = 0
        self._insert_number = 0
        self._delete_calls = 0

    @property
    def content(self) -> str:
        return self._content

    @property
    def get_calls(self) -> int:
        return self._get_calls

    @property
    def insert_calls(self) -> int:
        return self._insert_number

    @property
    def delete_calls(self) -> int:
        return self._delete_calls

    def get(self) -> str:
        self._get_calls += 1
        return self._content

    # noinspection PyUnusedLocal
    def delete(self, first: int, last: int=None) -> None:
        self._delete_calls += 1

    # noinspection PyUnusedLocal
    def insert(self, index: int, string: str) -> None:
        self._insert_number += 1
        self._content = string
