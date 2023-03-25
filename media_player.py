import logging
from zankpy import ZankControlClient
from homeassistant.components.media_player import MediaPlayerEntity
from homeassistant.components.media_player.const import (
    SUPPORT_PLAY,
    SUPPORT_PAUSE,
    SUPPORT_STOP,
    SUPPORT_PREVIOUS_TRACK,
    SUPPORT_NEXT_TRACK,
    SUPPORT_VOLUME_STEP,
    SUPPORT_VOLUME_MUTE,
)
from homeassistant.const import (
    CONF_HOST,
    CONF_NAME,
    CONF_PORT,
)

_LOGGER = logging.getLogger(__name__)

SUPPORTED_FEATURES = (
    SUPPORT_PLAY
    | SUPPORT_PAUSE
    | SUPPORT_STOP
    | SUPPORT_PREVIOUS_TRACK
    | SUPPORT_NEXT_TRACK
    | SUPPORT_VOLUME_STEP
    | SUPPORT_VOLUME_MUTE
)

def setup_platform(hass, config, add_entities, discovery_info=None):
    # Use the entry data instead of config
    entry_data = discovery_info

    name = entry_data.get(CONF_NAME, "Zank Media Player")
    host = entry_data[CONF_HOST]
    port = entry_data[CONF_PORT]

    add_entities([ZankMediaPlayer(name, host, port)])

class ZankMediaPlayer(MediaPlayerEntity):
    def __init__(self, name, host, port):
        self._name = name
        self._client = ZankControlClient(host, port)
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def supported_features(self):
        return SUPPORTED_FEATURES

    # Implement the media player control methods, for example:
    def media_play(self):
        self._client.send_command("mediaPlayPause")
        self._state = "playing"

    def media_pause(self):
        self._client.send_command("mediaPlayPause")
        self._state = "paused"

    def media_stop(self):
        self._client.send_command("mediaPlayPause")
        self._state = "idle"

    def media_previous_track(self):
        self._client.send_command("mediaPrevious")

    def media_next_track(self):
        self._client.send_command("mediaNext")

    def volume_up(self):
        self._client.send_command("volumeUp")

    def volume_down(self):
        self._client.send_command("volumeDown")

    def mute_volume(self, mute):
        self._client.send_command("volumeMute")

    def turn_on(self):
        self._client.send_command("lockScreen")

    def turn_off(self):
        self._client.send_command("lockScreen")

    def media_play_pause(self):
        self._client.send_command("mediaPlayPause")

    def channel_up(self):
        self._client.send_command("channelUp")

    def channel_down(self):
        self._client.send_command("channelDown")

    def send_command(self, command):
        self._client.send_command(command)


