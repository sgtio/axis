"""Python library to enable Axis devices to integrate with Home Assistant."""

import logging

_LOGGER = logging.getLogger(__name__)

FW_UPGRADE_URL = '/axis-cgi/firmwareupgrade.cgi'
UPSTREAM_FW_URL = 'https://www.google.com'

class DeviceManager():
    """Handle configuration of a device."""

    def __init__(self, configuration, vapix, session):
        """Setup stream manager."""
        self.vapix = vapix
        self.config = configuration
        self.session = session

    async def retrieve_latest_fw_version(self) -> str:
        """Retrieve the latest firmware version for the given device."""
        resp = await self.session.get(UPSTREAM_FW_URL)
        return await resp.text()

    def firmware_upgrade(self, path: str, clean_flash: bool = False):
        """Upgrade the Axis device with the given firmware."""
        with open(path, 'rb') as firmware:
            payload = {
                'type' : 'factorydefault' if clean_flash else 'normal',
                'file' : firmware,
                }
            self.vapix.request('post', FW_UPGRADE_URL, data=payload)
