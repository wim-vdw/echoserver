from flask import Blueprint
from datetime import datetime, timezone
import socket

echoserver_bp = Blueprint('echoserver', __name__)


@echoserver_bp.route('/')
def index():
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
        'hostname': host_name,
        'host_ip': host_ip,
        'local_timezone': local_timezone,
        'local_time': local_time,
        'local_time_utc': local_time_utc,
    }

    return result
