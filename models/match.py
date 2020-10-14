from datetime import datetime
from typing import Any, Dict

from constants import (
    AGES,
    GAME_TYPES,
    LEADERBOARD_TYPES,
    MAP_SIZES,
    MAP_TYPES,
    RATING_TYPES,
    RESOURCES,
    SPEEDS,
    VICTORY_TYPES,
    VISIBILITIES,
)
from helpers.date import timestamp_to_datetime


class Match:
    match_id: str = ""
    match_uuid: str = ""
    lobby_id: str = ""
    name: str = ""
    num_players: int = 0
    num_ais: int = 0
    game_type: str = ""
    map_type: str = ""
    map_size: str = ""
    starting_age: str = ""
    ending_age: str = ""
    population_limit: int = 0
    resources: str = ""
    speed: str = ""
    victory: str = ""
    visibility: str = ""
    ranked: bool = False
    leaderboard: str = ""
    rating_type: str = ""
    average_rating: int = 0
    opened: datetime = datetime.now()
    started: datetime = datetime.now()
    finished: datetime = datetime.now()

    def __init__(self, data: Dict[str, Any]) -> None:
        self.match_id = data["match_id"]
        self.match_uuid = data["match_uuid"]
        self.lobby_id = data["lobby_id"]
        self.name = data["name"]
        self.num_players = data["num_players"]
        self.game_type = GAME_TYPES[data["game_type"]]
        self.map_type = MAP_TYPES[data["map_type"]]
        self.map_size = MAP_SIZES[data["map_size"]]
        self.starting_age = AGES[data["starting_age"]]
        self.ending_age = AGES[data["ending_age"]]
        self.population_limit = data["pop"]
        self.resources = RESOURCES[data["resources"]]
        self.speed = SPEEDS[data["speed"]]
        self.victory = VICTORY_TYPES[data["victory"]]
        self.visibility = VISIBILITIES[data["visibility"]]
        self.ranked = data["ranked"]
        self.leaderboard = LEADERBOARD_TYPES[data["leaderboard_id"]]
        self.rating_type = RATING_TYPES[data["rating_type"]]
        self.average_rating = data["average_rating"]
        self.opened = timestamp_to_datetime(data["opened"])
        if data["started"] is not None:
            self.started = timestamp_to_datetime(data["started"])
        if data["finished"] is not None:
            self.finished = timestamp_to_datetime(data["finished"])

    def set_num_ais(self, players):
        self.num_ais = len(players) - self.num_players

    def __str__(self) -> str:
        return f"""
            Match
                ---------------------------------------
                ID: {self.match_id}
                UUID: {self.match_uuid}
                Lobby ID: {self.lobby_id}
                Name: {self.name}
                No. Players: {self.num_players}
                Game Type: {self.game_type}
                Map Type: {self.map_type}
                Map Size: {self.map_size}
                Starting Age: {self.starting_age}
                Ending Age: {self.ending_age}
                Population Limit: {self.population_limit}
                Resources: {self.resources}
                Speed: {self.speed}
                Victory: {self.victory}
                Visibility: {self.visibility}
                Ranked: {self.ranked}
                Leaderboard: {self.leaderboard}
                Rating Type: {self.rating_type}
                Average Rating: {self.average_rating}
                Opened: {self.opened}
                Started: {self.started}
                Finished: {self.finished}
        """
