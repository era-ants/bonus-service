from fastapi import status

ERROR_MSG = {
    status.HTTP_404_NOT_FOUND: {
        "content": {"application/json": {}},
        "description": "Could not found any users"
    }
}
