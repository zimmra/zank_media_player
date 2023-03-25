import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_HOST, CONF_PORT

from . import DOMAIN

DEFAULT_PORT = 1028

DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_HOST, description={"title": "IP Address"}): str,
        vol.Optional(CONF_PORT, default=DEFAULT_PORT, description={"title": "Port"}): int,
    }
)

class ZankMediaPlayerConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        
        if user_input is not None:
            await self.async_set_unique_id(user_input[CONF_HOST])
            self._abort_if_unique_id_configured()

            try:
                # Validate the input and create the config entry if valid.
                return self.async_create_entry(title=user_input[CONF_HOST], data=user_input)
            except Exception:
                errors["base"] = "unknown_error"

        return self.async_show_form(step_id="user", data_schema=DATA_SCHEMA, errors=errors)
