import os
from math import inf

from libs.VideoFile import VideoFile


class TvFile(VideoFile):

    _SEASON_EPISODE = VideoFile._TYPE_RE

    def __init__(self, src: str, src_name: str):
        self._season = None
        self._episode = None

        super().__init__(src, src_name)

    @property
    def season(self):
        return int(self._season) if self._season else None

    @property
    def episode(self):
        return int(self._episode) if self._episode else None


    @property
    def base_name(self):
        return (self._clean_src_name
                + ("[S{:0>2}E{:0>2}]".format(self._season, self._episode)
                   if self._season and self._episode else "")
                + ("[{}]".format(self.year) if self.year else "")
                + ("[{}]".format(self.res) if self.res else "")
                + "." + self.extension
                )

    @property
    def dest_path(self):
        return os.path.join(super().dest_path, ("Season {:0>2}".format(self._season) if self._season else ""))

    def _get_file_info(self):
        self._get_season_and_episode()
        super(TvFile, self)._get_file_info()

    def _get_season_and_episode(self):
        value = self._search(self._SEASON_EPISODE)
        if value:
            self._season, self._episode = value.lower().strip("s").split("e")

    def _get_src_name_trim_index(self):
        values = list(filter(None.__ne__, [self._year, self._res]))

        if self._episode and self._season:
            values.append("s{}e{}".format(self._season, self._episode))

        index = inf
        for substring in values:

            try:
                position = self._src_name.lower().index(substring.lower())

                if position < index:
                    index = position

            except ValueError:
                pass

        return index
