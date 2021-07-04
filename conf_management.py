import config as cfg


def get_db_user() -> str:
    return cfg.POSTGRE_USER


def get_db_pass() -> str:
    return cfg.POSTGRE_PASS


def get_db_host() -> str:
    return cfg.POSTGRE_HOST


def get_db_database() -> str:
    return cfg.POSTGRE_DATABASE


def get_db_provider() -> str:
    return cfg.POSTGRE_PROVIDER
