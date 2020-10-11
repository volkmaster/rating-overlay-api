import logging
from typing import Tuple

from flask import Blueprint, Response, jsonify

from helpers.api import get_ids_from_query_string
from helpers.asgi import get_loop, wait
from logic.fetch_data import (
    FetchDataException,
    fetch_apply_history,
    fetch_apply_leaderboard,
    fetch_last_match,
)

bp = Blueprint("match", __name__, url_prefix="/match")
logger = logging.getLogger(__name__)
loop = get_loop()


@bp.route("/", methods=("GET",))
def get() -> Tuple[Response, int]:
    ids = get_ids_from_query_string()
    if "profile_id" not in ids and "steam_id" not in ids:
        logging.error(" Missing both profile_id and steam_id query parameters.")
        return (
            jsonify({"message": "Please provide either profile_id or steam_id query parameter."}),
            400,
        )

    try:
        params = {"game": "aoe2de", **ids, "count": 1}
        match, players, leaderboard_id = wait(loop, fetch_last_match(params))
    except FetchDataException as e:
        logging.error(f" Player not found: {ids}")
        return jsonify({"message": e.message}), 404

    params = {"game": "aoe2de", "leaderboard_id": leaderboard_id}
    wait(loop, fetch_apply_leaderboard(params, players))
    wait(loop, fetch_apply_history(params, players))

    return jsonify({"match": match, "players": players}), 200
