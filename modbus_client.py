"""
Connecteur Modbus — à implémenter en Phase 6, pour la lecture des
onduleurs et automates industriels compatibles Modbus TCP/RTU.
"""
from config.settings import settings

MODBUS_HOST = settings.modbus_host
MODBUS_PORT = settings.modbus_port

# TODO Phase 6 : implémenter la connexion pymodbus (ModbusTcpClient),
# le mapping des registres par équipement, et la classe
# ModbusDataSource(EnergyDataSource).
