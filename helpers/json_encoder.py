from datetime import datetime
from json import JSONEncoder
from typing import Any, Dict, Union


class CustomJSONEncoder(JSONEncoder):
    def default(self, o: Any) -> Union[str, Dict[str, Any]]:
        if isinstance(o, datetime):
            return o.isoformat()

        return o.__dict__
