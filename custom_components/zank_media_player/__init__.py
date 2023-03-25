from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.const import CONF_HOST, CONF_PORT
from .media_player import async_setup_entry

DOMAIN = "zank_media_player"

async def async_setup(hass: HomeAssistant, config: dict):
    hass.data.setdefault(DOMAIN, {})
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    hass.data[DOMAIN][entry.entry_id] = entry.data
    
    # Forward the setup to the media_player platform
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "media_player")
    )
    
    hass.async_create_task(async_setup_entry(hass, entry, async_add_entities))
    
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    # Forward the unload to the media_player platform
    await hass.config_entries.async_forward_entry_unload(entry, "media_player")
    
    hass.data[DOMAIN].pop(entry.entry_id)
    return True