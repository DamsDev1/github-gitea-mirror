import os
import json

config_path = "config/config.json"

if not os.path.exists(config_path) or os.path.getsize(config_path) == 0:
    # File does not exist or is empty
    config_data = {
        "github": {
            "username": "",
            "accesstoken": ""
        },
        "gitea": {
            "host": "",
            "accesstoken": "",
            "username": "",
            "default_userpassword": "RY7VpBD62P7964c4c3e2c8e$mSz%2GAM82hv68yUbHc4@Gdw8c%f^W3*qd4c3e2c8ef*8a6b^rKy",
            "gist": {
                "prefix": "gist",
                "surfix": ""
            }
        },
        "local_cache": {
            "enabled": True,
            "file_path": "cache.json"
        },
        "repomap": {},
        "blacklist": [],
        "gistsSource": True,
        "gistsStared": True,
        "repositoryStared": True,
        "repositorySource": True,
        "repositoryForked": True
    }

    with open(config_path, 'w') as file:
        json.dump(config_data, file, indent=2)