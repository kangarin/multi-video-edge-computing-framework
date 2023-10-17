import sys
from app_prototype import AppPrototype

if __name__ == "__main__":
    import json
    config_path = "./configs/myapp.json"
    config = None
    with open(config_path, "r") as f:
        config = json.load(f)
    print(config)
    app = AppPrototype(config)
    app.run()