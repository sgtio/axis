"""Python library to enable Axis devices to integrate with Home Assistant."""

import logging
from .param_cgi import Properties

_LOGGER = logging.getLogger(__name__)

FW_UPGRADE_URL= '/axis-cgi/firmwareupgrade.cgi'

class DeviceManager(object):
    """Handle configuration of a device."""

    def __init__(self, vapix):
        """Setup stream manager."""
        self.vapix = vapix

    def firmware_upgrade(self, path: str, clean_flash: bool = False):
        """Upgrade the Axis device with the given firmware"""
        with open(path, 'rb') as firmware:
            payload = {
                    'type' : 'factorydefault' if clean_flash else 'normal',
                    'file' : firmware,
                    }
            self.vapix.request('post', FW_UPGRADE_URL, data=payload)
