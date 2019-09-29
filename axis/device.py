"""Python library to enable Axis devices to integrate with Home Assistant."""

import logging

from .configuration import Configuration
from .vapix import Vapix
from .streammanager import StreamManager
from .event_stream import EventManager
from .devicemanager import DeviceManager

_LOGGER = logging.getLogger(__name__)


class AxisDevice:
    """Creates a new Axis device.self."""

    def __init__(self, **kwargs) -> None:
        """Initialize device functionality."""
        self.config = Configuration(**kwargs)
        self.vapix = Vapix(self.config)
        self.stream = StreamManager(self.config)
        self.event = None
        self.devicemanager = DeviceManager(self.config, self.vapix)

    def start(self) -> None:
        """Start functionality of device."""
        self.stream.start()

    def stop(self) -> None:
        """Stop functionality of device."""
        self.stream.stop()

    def enable_events(self, event_callback=None) -> None:
        """Enable events for stream."""
        self.event = EventManager(event_callback)
        self.stream.event = self.event
