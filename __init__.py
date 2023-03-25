from homeassistant import config_entries
from .config_flow import ZankMediaPlayerConfigFlow

DOMAIN = "zank_media_player"

async def async_setup(hass, config):
    hass.config_entries.async_register_flow_handler(DOMAIN, ZankMediaPlayerConfigFlow)
    return True

async def async_setup_entry(hass, entry):
    hass.helpers.discovery.async_load_platform("media_player", DOMAIN, entry.data, {})
    return True
