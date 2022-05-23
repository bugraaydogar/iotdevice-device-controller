import requests
from .helpers import SnapdAdapter

class SnapdClient():
    def __init__(self):
        self.session = requests.Session()
        self.session.mount("http://snapd/", SnapdAdapter())
    
    def snap_system_info(self):
        response = self.session.get("http://snapd/v2/system-info")
        return response.json()

    def refresh(self):
        response = self.session.post("http://snapd/v2/snaps", {"action": "refresh"})
        return response.json()

    def revert(self, snaps):
        payload = {
            "action":"revert",
            "snaps" : snaps
        }
        response = self.session.post("http://snapd/v2/snaps", payload)
        return response.json()
