create_pet = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "type": "integer"
        },
        "category": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "name": {
                    "type": "string"
                }
            },
            "additionalProperties": False,
            "required": [
                "id",
                "name"
            ]
        },
        "name": {
            "type": "string"
        },
        "photoUrls": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "tags": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer"
                    },
                    "name": {
                        "type": "string"
                    }
                },
                "additionalProperties": False,
                "required": [
                    "id",
                    "name"
                ]
            }
        },
        "status": {
            "type": "string"
        }
    },
    "additionalProperties": False,
    "required": [
        "id",
        "category",
        "name",
        "photoUrls",
        "tags",
        "status"
    ]
}

update_pet = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "name": {
            "type": "string"
        }
    },
    "additionalProperties": False,
    "required": [
        "name"
    ]
}
