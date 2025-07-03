# System Anomaly Detector

[![Language](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A project for the "Data Collection and Machine Learning" course. This repository contains an end-to-end anomaly detector for a standalone system, built with Python.

The software monitors system performance indicators, uses a machine learning model to classify behavior as 'Normal' or 'Anomalous', and provides real-time alerts.

## Features

- **Real-time Monitoring:** Collects CPU, RAM, and process metrics every second.
- **Anomaly Simulation:** Includes a script to simulate high CPU load to generate training data.
- **ML-Powered Detection:** Uses a trained Random Forest model to detect anomalies.
- **Modular Structure:** Code is organized into modules for monitoring, simulation, and detection.

## Project Structure

```
/
├── anomaly_detector/      # Main application package
├── scripts/               # Helper scripts (data collection, training)
├── main_detector.py       # Main entry point for the real-time detector
├── .gitignore             # Git ignore file
├── README.md              # This file
└── requirements.txt       # Python dependencies
```

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd anomaly-detector
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

The project is divided into three main stages:

### Stage 1: Collect Training Data

Run the `collect_data.py` script to generate a `training_data.csv` file. This script will guide you through collecting data for both normal and anomalous system states.

```bash
python scripts/collect_data.py
```
Follow the on-screen instructions (it will ask you to run the anomaly simulation in a separate terminal).

### Stage 2: Train the Model

Once you have `training_data.csv`, train the machine learning model by running:

```bash
python scripts/train_model.py
```
This script will load the data, train a Random Forest classifier, and save the trained model as `model.joblib`.

### Stage 3: Run the Real-Time Detector

With the trained model ready, start the live anomaly detector:

```bash
python main_detector.py
```
The detector will start monitoring your system and print "ANOMALY DETECTED!" in red if system behavior deviates from the learned norm.
