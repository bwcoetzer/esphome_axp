import esphome.codegen as cg
from esphome.components import uart
import esphome.config_validation as cv
from esphome.const import CONF_ID

DEPENDENCIES = ["uart"]
CODEOWNERS = ["@andreashergert1984"]
AUTO_LOAD = ["binary_sensor", "text_sensor", "sensor", "switch", "output"]
MULTI_CONF = True

CONF_PIPSOLAR_ID = "pipsolar_axp_id"

pipsolar_axp_ns = cg.esphome_ns.namespace("pipsolar_axp")
PipsolarComponent = pipsolar_axp_ns.class_("Pipsolar_axp", cg.Component)

PIPSOLAR_COMPONENT_SCHEMA = cv.Schema(
    {
        cv.Required(CONF_PIPSOLAR_ID): cv.use_id(PipsolarComponent),
    }
)

CONFIG_SCHEMA = cv.All(
    cv.Schema({cv.GenerateID(): cv.declare_id(PipsolarComponent)})
    .extend(cv.polling_component_schema("1s"))
    .extend(uart.UART_DEVICE_SCHEMA)
)


def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)
    yield uart.register_uart_device(var, config)