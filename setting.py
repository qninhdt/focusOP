import yaml

name = 0
public_port = 0
api_port = 0
min_tracking_confidence = 0
min_detection_confidence = 0

with open("config/settings.yml","r") as file:
    data = yaml.safe_load(file)
    
    name = data["server"]["name"]
    public_port = data["server"]["public-port"]
    api_port = data["server"]["api-port"]

    min_detection_confidence = data["hand-tracker"]["min_detection_confidence"]
    min_tracking_confidence = data["hand-tracker"]["min_tracking_confidence"]
