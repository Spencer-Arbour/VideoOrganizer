from typing import Union


class TvDbResponseParser:

    @classmethod
    def get_show_id(cls, response: dict, year_premiered: str=None) -> Union[int, None]:
        data = response.get("data", None)

        if not data:
            return None

        if year_premiered:
            return cls._get_shows_premiering_that_year(data, year_premiered)

        else:
            return cls._newest_show(data)

    @staticmethod
    def _get_shows_premiering_that_year(data: list, year_premiered: str) -> int:
        # This could fail if more then one show with the same name premiered in the same year
        # google search did not come up with any results so this will be done later if needed
        for show in data:
            first_aired = show.get("firstAired", None)

            if first_aired:
                if first_aired.split("-", 1)[0] == year_premiered:
                    return show.get("id")

    @staticmethod
    def _newest_show(data: list):
        most_recent_index = 0

        for index, show in enumerate(data):
            first_aired = show.get("firstAired", None)

            if first_aired:
                if first_aired > most_recent_index:
                    most_recent_index = index

        return data[most_recent_index].get("id")

    @classmethod
    def get_episode_name(cls, episodes: dict, season_num: int, episode_num: int) -> str:
        data = episodes.get("data", None)
        if data:
            for episode in data:

                if cls._is_correct_episode(episode, season_num, episode_num):
                    return episode.get("episodeName", None)

    @staticmethod
    def _is_correct_episode(episode: dict, season_num: int, episode_num: int) -> bool:
        return (
                episode.get("airedSeason", None) == season_num and
                episode.get("airedEpisodeNumber", None) == episode_num
        )


if __name__ == "__main__":
    x = TvDbResponseParser.get_show_id(({
  "data": [
    {
      "aliases": [],
      "banner": "graphical/80337-g13.jpg",
      "firstAired": "2007-07-19",
      "id": 80337,
      "network": "AMC",
      "overview": "In 1960s New York, alpha male Don Draper struggles to stay on top of the heap in the high-pressure world of Madison Avenue advertising firms. Aside from being one of the top ad men in the business, Don is also a family man, the father of young children.",
      "seriesName": "Mad Men",
      "slug": "mad-men",
      "status": "Ended"
    },
    {
      "aliases": [],
      "banner": "graphical/322780-g.jpg",
      "firstAired": "2017-01-09",
      "id": 322780,
      "network": "Smithsonian Channel",
      "overview": "Follow the evolution of advertising from the 1950s through the 1980s, via interviews with the industry's top ad executives, and through classic ads and commercials.",
      "seriesName": "The Real Mad Men of Advertising",
      "slug": "the-real-mad-men-of-advertising",
      "status": "Ended"
    }
  ]
}))

    print(x)
