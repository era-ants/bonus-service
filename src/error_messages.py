from fastapi import status

ACCOUNT_ALREADY_EXIST = {
    'exception': {
        'status_code': status.HTTP_400_BAD_REQUEST,
        'detail': "Account already exist, try signup account with another client ID",
    },
    'api_docs': {
        status.HTTP_400_BAD_REQUEST: {
            "content": {"application/json": {}},
            "description": "Account already exist, try signup account with another client ID"
        }
    }
}

ACCOUNT_DOES_NOT_EXIST = {
    'exception': {
        'status_code': status.HTTP_404_NOT_FOUND,
        'detail': "Account does not exist, try another Client ID",
    },
    'api_docs': {
        status.HTTP_404_NOT_FOUND: {
            "content": {"application/json": {}},
            "description": "Account does not exist, try another Client ID"
        }
    }
}

