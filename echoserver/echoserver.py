from flask import Blueprint, request
from datetime import datetime, timezone
import socket

echoserver_bp = Blueprint('echoserver', __name__)


@echoserver_bp.route('/', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
@echoserver_bp.route('/<path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def index(path=None):
    method = request.method
    path = request.path
    query_string = request.query_string.decode('utf-8')
    host_name = socket.gethostname()
    try:
        host_ip = socket.gethostbyname(host_name)
    except socket.gaierror as err:
        host_ip = 'could not resolve hostname'
    now = datetime.now()
    local_timezone = str(now.astimezone().tzinfo)
    local_time = now.astimezone().isoformat()
    local_time_utc = now.astimezone(timezone.utc).isoformat()
    result = {
        'path': path,
        'method': method,
        'query_string': query_string,
        'server_info': {
            'hostname': host_name,
            'host_ip': host_ip,
            'timezone': local_timezone,
            'time': local_time,
            'time_utc': local_time_utc,
        }
    }

    return result
