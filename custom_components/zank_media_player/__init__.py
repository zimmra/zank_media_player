from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .media_player import ZankMediaPlayer

DOMAIN = "zank_media_player"

async def async_setup(hass: HomeAssistant, config: dict):
    hass.data.setdefault(DOMAIN, {})
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    media_player = ZankMediaPlayer(hass, entry.data)
    await media_player.async_added_to_hass()
    
    hass.data[DOMAIN][entry.entry_id] = media_player
    hass.helpers.dispatcher.async_dispatcher_send(DOMAIN, entry.entry_id)
    
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    media_player = hass.data[DOMAIN].pop(entry.entry_id)
    await media_player.async_will_remove_from_hass()

    return True
