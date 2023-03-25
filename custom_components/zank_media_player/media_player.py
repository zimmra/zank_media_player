import logging
import string
import secrets
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
    SUPPORT_VOLUME_UP,
    SUPPORT_VOLUME_DOWN,
)
from homeassistant.const import (
    STATE_IDLE,
    STATE_PLAYING,
    STATE_PAUSED,
    STATE_UNKNOWN,
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
    | SUPPORT_VOLUME_UP
    | SUPPORT_VOLUME_DOWN
)
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities):
    ip_address = config_entry.data[CONF_HOST]
    port = config_entry.data[CONF_PORT]

    media_player = ZankMediaPlayer(hass, ip_address, port, config_entry)
    
    hass.data[DOMAIN][config_entry.entry_id] = media_player
    hass.helpers.dispatcher.async_dispatcher_send(DOMAIN, config_entry.entry_id)

    async_add_entities([media_player])
    return True

class ZankMediaPlayer(MediaPlayerEntity):
    def __init__(self, hass, ip_address, port, config_entry):
        self.hass = hass
        self._client = ZankControlClient(ip_address, port)
        self._config_entry = config_entry
        self._attr_name = f"Zank Media Player ({ip_address})"
        random_suffix = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(5))
        self._attr_unique_id = f"{ip_address}-{random_suffix}"

    async def async_added_to_hass(self):
        self.hass.async_create_task(
            self.hass.config_entries.async_forward_entry_setup(self._config_entry, "media_player")
        )

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return STATE_UNKNOWN

    @property
    def supported_features(self):
        return SUPPORTED_FEATURES

    # Implement the media player control methods, for example:
    def media_play(self):
        self._client.send_command("mediaPlayPause")

    def media_pause(self):
        self._client.send_command("mediaPlayPause")

    def media_stop(self):
        self._client.send_command("mediaPlayPause")

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


