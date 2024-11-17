# Drone Jamming Detection and Mitigation System

This repository contains a Python-based system designed to detect and mitigate drone jamming attacks. The system uses signal processing, machine learning, encryption, and communication channel management to ensure secure and reliable drone operations even under jamming conditions.

## Project Overview

The system includes:
- Signal Generation and Detection: Generates simulated drone communication signals and detects anomalies using Fast Fourier Transform (FFT).
- Machine Learning for Jamming Detection: Trains a model to recognize jamming patterns and switch communication channels accordingly.
- Secure Communication: Implements encryption to ensure secure message transmission.
- Redundant Communication: Switches channels and employs frequency hopping to avoid jamming interference.
- Recovery Strategy: Implements a recovery mechanism in case of jamming.

## Requirements

- Python 3.x
- Required Python libraries:
  - `numpy`
  - `scipy`
  - `sklearn`
  - `cryptography`
  - `matplotlib`
  - `graphviz`
  
You can install these dependencies using pip:
pip install numpy scipy scikit-learn cryptography matplotlib graphviz


1. Clone the repository
git clone https://github.com/your-username/drone-jamming-detection.git
cd drone-jamming-detection
2. Open the file tempCodeRunnerFile.py in your preferred Python IDE or text editor.
3. Run the script. You can interact with the system by inputting the frequency and noise level of the simulated signal. Example:
python tempCodeRunnerFile.py
4. The script will prompt you for the signal frequency (Hz) and noise level. You can also choose to view the signal plot or generate an advanced feedback flowchart.
5. Logs for the operations will be stored in drone_jamming_log.log. You can check this file to track the system's activities and detect any anomalies or jamming events.

# Code Explanation
1. Signal Generation and Detection:
The system simulates drone communication signals and uses the FFT to analyze the frequency spectrum. If an anomaly is detected (e.g., a jamming signal), the system will attempt to recover by switching communication channels.

2. Machine Learning Model:
A Random Forest Classifier is trained on simulated normal and jamming signals to recognize jamming patterns. When jamming is detected, the system switches to a backup channel to prevent disruption.

3. Encryption:
All messages transmitted during the simulation are encrypted using Fernet encryption to ensure secure communication.

4. Recovery Mechanism:
The system implements frequency hopping and channel switching as part of its recovery strategy in case of jamming.

# Log File
The system writes logs to a file named drone_jamming_log.log located in the same directory as the script. This log file tracks:

Signal anomaly detections
Jamming pattern detections
Channel switches
Encryption and decryption activities

# How to View the Flowchart
The system can generate a flowchart of the jamming detection and recovery process, which visualizes the steps taken when a jamming event is detected. To generate this flowchart, the system will prompt you for confirmation during execution.

The flowchart will be saved as advanced_feedback_flowchart_with_recovery.png in the working directory.

# Example Interaction
Enter the signal frequency (Hz, e.g., 50): 50
Enter the noise level (e.g., 0.1 for low noise, 1.5 for high noise): 1.5

Monitoring new signal...
Max amplitude detected: 120.53
Anomaly Detected: Potential Jamming Signal!
Switched to Channel 3 due to interference.
Frequency hopping: Switched to Channel 5
Recovery initiated: Switched to a new channel.
Message encrypted for secure transmission
Message decrypted successfully

Would you like to view the signal plot? (yes/no): yes
Would you like to generate advanced feedback flowchart with recovery details? (yes/no): yes

# License
Save this as `README.md` in your repository and make sure to adjust the GitHub link and any other details based on your actual repository information.

