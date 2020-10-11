from typing import Any, Dict, List, Optional

from constants import CIVILIZATIONS, COLORS


class Player:
    # player info
    is_ai: bool = False
    profile_id: str = ""
    steam_id: str = ""
    name: str = ""
    country: str = ""
    rank: int = 0
    rating: int = 0
    games: int = 0
    wins: int = 0
    losses: int = 0
    streak: int = 0

    # match info
    team: int = 0
    civilization: str = ""
    color: str = ""
    won: Optional[bool] = None

    def __init__(self, data: Dict[str, Any]) -> None:
        self.is_ai = data["profile_id"] is None and data["steam_id"] is None
        if not self.is_ai:
            self.profile_id = str(data["profile_id"])
            self.steam_id = data["steam_id"]
            self.name = data["name"]
            self.country = data["country"]

    def from_match(self, data: Dict[str, Any]) -> None:
        self.team = data["team"]
        self.civilization = CIVILIZATIONS[data["civ"]]
        self.color = COLORS[data["color"]]
        if data["won"] is not None:
            self.won = data["won"]

    def from_leaderboard(self, data: List[Dict[str, Any]]) -> None:
        if len(data) > 0:
            self.rank = data[0]["rank"]

    def from_history(self, data: List[Dict[str, Any]]) -> None:
        if len(data) > 0:
            self.rating = data[0]["rating"]
            self.wins = data[0]["num_wins"]
            self.losses = data[0]["num_losses"]
            self.games = self.wins + self.losses
            self.streak = data[0]["streak"]

    def __str__(self) -> str:
        return f"""
            Player
                ---------------------------------------
                Is AI: {self.is_ai}
                Profile ID: {self.profile_id}
                Steam ID: {self.steam_id}
                Name: {self.name}
                Country: {self.country}
                Rank: {self.rank}
                Rating: {self.rating}
                Games: {self.games}
                Wins: {self.wins}
                Losses: {self.losses}
                Streak: {self.streak}
                ---------------------------------------
                Team: {self.team}
                Civilization: {self.civilization}
                Color: {self.color}
        """
