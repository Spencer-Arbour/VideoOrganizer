import os
import re
from math import inf
from abc import ABC


class VideoFile(ABC):

    _TYPE_RE = re.compile(r"S[0-9]{1,2}E[0-9]{1,2}", re.I)
    _YEAR_RE = re.compile(r"\.20[0-9]{2}\.|\.1[7-9][0-9]{2}\.", re.I)
    _RES_RE = re.compile(r"1080p?|720p?", re.I)
    _SEEDER_INFO = re.compile("\[[0-9a-z.\s]+\]", re.I)

    def __init__(self, src: str, src_name: str):
        self._src = src
        self._src_name = src_name

        self._year = None
        self._res = None
        self._ext = None
        self._clean_src_name = None

        self._get_file_info()

    @property
    def src_file(self):
        return os.path.join(self._src, self._src_name)

    @property
    def res(self):
        if self._res:
            return self._res.lower() if self._res[-1].lower() == "p" else self._res + "p"
        return None

    @property
    def year(self):
        return self._year

    @property
    def extension(self):
        return self._ext

    @property
    def base_name(self):
        return (self._clean_src_name
                + ("[{}]".format(self.year) if self.year else "")
                + ("[{}]".format(self.res) if self.res else "")
                + "." + self.extension
                )

    @property
    def dest_path(self):
        return self._clean_src_name + (" [{}]".format(self._year) if self._year else "")

    def _get_file_info(self):
        self._get_resolution()
        self._get_year()
        self._get_extension()
        self._get_cleaned_src_name()

    def _get_extension(self):
        # No video formats with multiple parts ex .tar.gz
        # https://en.wikipedia.org/wiki/Video_file_format
        self._ext = self._src_name.rsplit(".", 1)[-1]

    def _get_year(self):
        year = self._search(self._YEAR_RE)
        if year:
            self._year = year[1:-1]

    def _get_resolution(self):
        self._res = self._search(self._RES_RE)

    def _get_cleaned_src_name(self):
        trim_index = self._get_src_name_trim_index()
        seeder_info = self._search(self._SEEDER_INFO, 0)

        self._clean_src_name = (
            (self._src_name[:trim_index] if trim_index != inf else self._src_name[:-len(self._ext)])
            .replace(str(seeder_info), "")
            .replace(".", " ")
            .strip("[({})] ")
            .title()
        )

    def _get_src_name_trim_index(self):
        index = inf
        for substring in list(filter(None.__ne__, [self._year, self._res])):
            if substring:
                try:
                    position = self._src_name.lower().index(substring.lower())
                    if position < index:
                        index = position
                except ValueError:
                    pass

        return index

    def _search(self, pattern, position=-1):
        value = pattern.findall(self._src_name)
        try:
            return value[position]

        except IndexError:
            return None

    def __str__(self):
        return self._src_name
