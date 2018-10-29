"""
Vault secrets engines endpoints

"""

from hvac.api.secrets_engines.azure import Azure
from hvac.api.secrets_engines.kv import Kv
from hvac.api.secrets_engines.kv_v1 import KvV1
from hvac.api.secrets_engines.kv_v2 import KvV2
from hvac.api.vault_api_category import VaultApiCategory

__all__ = (
    'Azure',
    'Kv',
    'KvV1',
    'KvV2',
    'SecretsEngines',
)


class SecretsEngines(VaultApiCategory):
    """Secrets Engines."""

    implemented_classes = [
        Azure,
        Kv,
    ]
    unimplemented_classes = [
        'Ad',
        'AliCloud',
        'AWS',
        'Azure',
        'Consul',
        'Database',
        'Gcp',
        'GcpKms',
        'Identity',
        'Nomad',
        'Pki',
        'RabbitMq',
        'Ssh',
        'TOTP',
        'Transit',
        'Cassandra',
        'MongoDb',
        'Mssql',
        'MySql',
        'PostgreSql',
    ]
