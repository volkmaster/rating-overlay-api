from typing import Any, Dict, Optional

import aiohttp
from flask import request


async def fetch(
    url: str, params: Optional[Dict[str, Any]] = None, content_type: str = "application/json"
) -> Any:
    if params is None:
        params = {}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            if response.status == 200:
                if content_type == "application/json":
                    return await response.json(content_type=None)
                if content_type == "text/plain":
                    return await response.text()

            return None


def get_ids_from_query_string() -> Dict[str, str]:
    profile_id, steam_id = request.args.get("profile_id"), request.args.get("steam_id")
    if profile_id:
        return {"profile_id": profile_id}
    if steam_id:
        return {"steam_id": steam_id}

    return {}
