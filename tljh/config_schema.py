config_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Littlest JupyterHub YAML config file",
    "definitions": {
        "Users": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "extra_user_groups": {"type": "object", "items": {"type": "string"}},
                "allowed": {"type": "array", "items": {"type": "string"}},
                "banned": {"type": "array", "items": {"type": "string"}},
                "admin": {"type": "array", "items": {"type": "string"}},
            },
        },
        "HTTP": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "address": {"type": "string", "format": "ipv4"},
                "port": {"type": "integer"},
            },
        },
        "HTTPS": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "enabled": {"type": "boolean"},
                "address": {"type": "string", "format": "ipv4"},
                "port": {"type": "integer"},
                "tls": {"$ref": "#/definitions/TLS"},
                "letsencrypt": {"$ref": "#/definitions/LetsEncrypt"},
            },
        },
        "LetsEncrypt": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "email": {"type": "string", "format": "email"},
                "domains": {
                    "type": "array",
                    "items": {"type": "string", "format": "hostname"},
                },
            },
        },
        "TLS": {
            "type": "object",
            "additionalProperties": False,
            "properties": {"key": {"type": "string"}, "cert": {"type": "string"}},
            "required": ["key", "cert"],
        },
        "Limits": {
            "description": "User CPU and memory limits.",
            "type": "object",
            "additionalProperties": False,
            "properties": {"memory": {"type": "string"}, "cpu": {"type": "integer"}},
        },
        "UserEnvironment": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "default_app": {
                    "type": "string",
                    "enum": ["jupyterlab", "classic"],
                    "default": "jupyterlab",
                }
            },
        },
    },
    "properties": {
        "additionalProperties": False,
        "user_environment": {"$ref": "#/definitions/UserEnvironment"},
        "users": {"$ref": "#/definitions/Users"},
        "limits": {"$ref": "#/definitions/Limits"},
        "https": {"$ref": "#/definitions/HTTPS"},
        "http": {"$ref": "#/definitions/HTTP"},
    },
}
