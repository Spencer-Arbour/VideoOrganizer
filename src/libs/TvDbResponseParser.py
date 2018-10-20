import re
from typing import Union

from gui.ShowChooser import ShowChooser


class TvDbResponseParser:
    _DATA = "data"
    _ID = "id"
    _FIRST_AIRED = "firstAired"
    _DATE_FORMAT = "%Y-%m-%d"
    _DATE_PATTERN = re.compile(r"[0-9]{4}-[0-1][0-2]-[0-3][0-9]", re.I)

    @classmethod
    def get_show_id(cls, search: str, response: dict, year_premiered: str=None) -> Union[int, None]:
        data = response.get(cls._DATA, None)

        if not data:
            return None

        shows = cls._get_possible_shows(data, year_premiered)
        return cls._get_id(search, shows)

    @classmethod
    def _get_possible_shows(cls, data: list, year_premiered: str=None) -> list:
        if year_premiered:
            return cls._get_shows_premiering_that_year(data, year_premiered)

        return data

    @classmethod
    def _get_shows_premiering_that_year(cls, data: list, year_premiered: str) -> list:
        # This could fail if more then one show with the same name premiered in the same year
        # google search did not come up with any results so this will be done later if needed
        shows = []
        for show in data:
            first_aired = show.get(cls._FIRST_AIRED, None)

            if first_aired:
                if first_aired.split("-", 1)[0] == year_premiered:
                    shows.append(show)

            else:
                shows.append(show)

        return shows

    @classmethod
    def _get_id(cls, search: str, shows: list, eliminate_shows_without_overview: bool=True) -> Union[None, int]:
        if not shows:
            return None

        elif len(shows) == 1:
            return shows[0].get(cls._ID, None)

        else:
            if eliminate_shows_without_overview:
                shows = cls._eliminate_shows_without_overview(shows)
                return cls._get_id(search, shows, False)

            show_chooser = ShowChooser(search, shows)

            show = show_chooser.show
            if show:
                return show.get(cls._ID, None)

            return None

    @classmethod
    def _eliminate_shows_without_overview(cls, shows: list):
        return [show for show in shows if show.get("overview", None)]

    #########################################

    @classmethod
    def get_episode_name(cls, episodes: dict, season_num: int, episode_num: int) -> Union[str, None]:
        data = episodes.get(cls._DATA, None)

        if not data:
            return None

        for episode in data:

            if type(episode) != dict:
                pass

            if cls._is_correct_episode(episode, season_num, episode_num):
                return episode.get("episodeName", None)

        return None

    @staticmethod
    def _is_correct_episode(episode: dict, season_num: int, episode_num: int) -> bool:
        return (
                episode.get("airedSeason", False) == season_num and
                episode.get("airedEpisodeNumber", False) == episode_num
        )
