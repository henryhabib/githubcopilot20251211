def read_sensor_data(file_path):
    import json
    with open(file_path, 'r') as file:
        return json.load(file)

def log_anomaly(anomaly):
    with open('anomalies.log', 'a') as log_file:
        log_file.write(anomaly + '\n')

def main():
    sensor_data = read_sensor_data('src/data/sensor_data.json')
    for reading in sensor_data:
        temperature = reading.get('temperature')
        voltage = reading.get('voltage')
        
        if temperature > 85:
            log_anomaly(f"Anomaly detected: Temperature {temperature}°C exceeds threshold")

if __name__ == "__main__":
    main()