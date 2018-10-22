import os
from math import inf

from libs.VideoFile import VideoFile


class TvFile(VideoFile):

    _SEASON_EPISODE = VideoFile._TYPE_RE

    def __init__(self, src: str, src_name: str):
        self._season_num = None
        self._episode_num = None

        self._episode_name = None

        super().__init__(src, src_name)

    @property
    def season_num(self):
        return int(self._season_num) if self._season_num else None

    @property
    def episode_num(self):
        return int(self._episode_num) if self._episode_num else None

    @property
    def episode_name(self):
        return self._episode_name

    @episode_name.setter
    def episode_name(self, episode_name):
        self._episode_name = episode_name

    @property
    def base_name(self):
        return (self._clean_src_name
                + ("[S{:0>2}E{:0>2}]".format(self._season_num, self._episode_num)
                   if self._season_num and self._episode_num else "")
                + (str(self._episode_name).strip() if self._episode_name else "")
                + ("[{}]".format(self._year) if self._year else "")
                + ("[{}]".format(self._res) if self._res else "")
                + "." + self.extension
                )

    @property
    def dest_path(self):
        return os.path.join(super().dest_path, ("Season {:0>2}".format(self._season_num) if self._season_num else ""))

    def _get_file_info(self):
        self._get_season_and_episode()
        super(TvFile, self)._get_file_info()

    def _get_season_and_episode(self):
        value = self._search(self._SEASON_EPISODE)
        if value:
            self._season_num, self._episode_num = value.lower().strip("s").split("e")

    def _get_src_name_trim_index(self):
        values = list(filter(None.__ne__, [self._year, self._res]))

        if self._episode_num and self._season_num:
            values.append("s{}e{}".format(self._season_num, self._episode_num))

        index = inf
        for substring in values:

            try:
                position = self._src_name.lower().index(substring.lower())

                if position < index:
                    index = position

            except ValueError:
                pass

        return index
