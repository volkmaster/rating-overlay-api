import asyncio
from typing import Any, Dict, List, Tuple

from constants import API_URL
from helpers.api import fetch
from models.match import Match
from models.player import Player


class FetchDataException(Exception):
    message: str

    def __init__(self, message: str = "Data fetching failed."):
        super().__init__(message)
        self.message = message


async def fetch_last_match(params: Dict[str, Any]) -> Tuple[Match, List[Player], int]:
    response = await fetch(f"{API_URL}/player/matches", params)
    if response is None or len(response) == 0:
        raise FetchDataException("Player not found.")

    match = Match(response[0])

    players = [Player(p) for p in response[0]["players"]]
    for i, item in enumerate(response[0]["players"]):
        players[i].from_match(item)

    leaderboard_id = response[0]["leaderboard_id"] or 3

    return match, players, leaderboard_id


async def fetch_apply_leaderboard(params: Dict[str, Any], players: List[Player]) -> None:
    leaderboard = await asyncio.gather(
        *[
            fetch(f"{API_URL}/leaderboard", params={**params, "profile_id": p.profile_id})
            for p in players
            if not p.is_ai
        ]
    )
    for i, item in enumerate(leaderboard):
        players[i].from_leaderboard(item["leaderboard"])


async def fetch_apply_history(params: Dict[str, Any], players: List[Player]) -> None:
    history = await asyncio.gather(
        *[
            fetch(
                f"{API_URL}/player/ratinghistory",
                params={**params, "profile_id": p.profile_id, "count": 1},
            )
            for p in players
            if not p.is_ai
        ]
    )

    for i, item in enumerate(history):
        players[i].from_history(item[0])
