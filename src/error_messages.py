from fastapi import status

ACCOUNT_ALREADY_EXIST = {
    'exception': {
        'status_code': status.HTTP_404_NOT_FOUND,
        'detail': "Account already exist, try signup account with another client ID",
    },
    'api_docs': {
        status.HTTP_404_NOT_FOUND: {
            "content": {"application/json": {}},
            "description": "Account already exist, try signup account with another client ID"
        }
    }
}
