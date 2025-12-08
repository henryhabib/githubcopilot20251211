def read_sensor_data(file_path):
    import json
    with open(file_path, 'r') as file:
        return json.load(file)

def log_anomaly(anomaly):
    import logging
    logging.basicConfig(filename='anomalies.log', level=logging.INFO)
    logging.info(anomaly)