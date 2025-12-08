# Sensor Data Analyzer

This project is designed to analyze sensor data for anomalies. It reads sensor data from a JSON file and logs any anomalies based on specified conditions.

## Project Structure

```
sensor-data-analyzer
├── src
│   ├── main.py          # Entry point of the application
│   ├── utils.py         # Utility functions for reading data and logging anomalies
│   └── data
│       └── sensor_data.json  # Sample sensor data in JSON format
├── requirements.txt      # Dependencies required for the project
└── README.md             # Documentation for the project
```

## Getting Started

### Prerequisites

Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/sensor-data-analyzer.git
   cd sensor-data-analyzer
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

### Running the Application

To run the application, execute the following command:
```
python src/main.py
```

### Sample Data

The application uses sample sensor data located in `src/data/sensor_data.json`. You can modify this file to test different scenarios.

### Logging

Anomalies will be logged based on the following conditions:
- Temperature readings greater than 85°C
- Voltage readings less than 0.9V

### Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.

### License

This project is licensed under the MIT License. See the LICENSE file for details.