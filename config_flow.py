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
    async def async_step_user(self, user_input=None):
        errors = {}

        if user_input is not None:
            host = user_input[CONF_HOST]
            port = user_input[CONF_PORT]

            # TODO: Validate the connection with the media player before creating the entry
            return self.async_create_entry(title=host, data=user_input)

        return self.async_show_form(
            step_id="user", data_schema=DATA_SCHEMA, errors=errors
        )