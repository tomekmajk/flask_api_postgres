from flask_api import status

def http_response(data: dict, statuscode: status=status.HTTP_200_OK):
    return (data,statuscode)
