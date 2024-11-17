import numpy as np
from scipy.fft import fft
from sklearn.ensemble import RandomForestClassifier
from cryptography.fernet import Fernet
import logging
import random
import matplotlib.pyplot as plt
from graphviz import Digraph
import time

# Setting up logging for activity tracking
logging.basicConfig(filename='drone_jamming_log.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Generate simulated drone communication signals with user-defined parameters
def generate_signal(frequency=50, noise_level=0.1):
    time_points = np.linspace(0, 1, 500)
    signal = np.sin(2 * np.pi * frequency * time_points)  # Simulated base frequency signal
    noise = noise_level * np.random.normal(size=time_points.shape)
    return signal + noise

# Signal Processing - Detects anomalies in frequency spectrum
def detect_anomaly(signal, threshold=100):
    fft_values = np.abs(fft(signal))
    max_amplitude = np.max(fft_values)
    logging.info(f"Max amplitude detected: {max_amplitude}")
    print(f"Max amplitude detected: {max_amplitude}")
    if max_amplitude > threshold:
        logging.warning("Anomaly Detected: Potential Jamming Signal!")
        print("Anomaly Detected: Potential Jamming Signal!")
        return True, max_amplitude
    return False, max_amplitude

# Train Machine Learning Model to Recognize Jamming Patterns
def train_jamming_detector():
    normal_signals = [generate_signal(noise_level=0.1) for _ in range(50)]
    jammed_signals = [generate_signal(noise_level=1.5) for _ in range(50)]
    
    X = normal_signals + jammed_signals
    y = [0] * 50 + [1] * 50  # 0 = normal, 1 = jamming

    clf = RandomForestClassifier()
    clf.fit(X, y)
    logging.info("Machine Learning Jamming Detector Trained Successfully")
    print("Machine Learning Jamming Detector Trained Successfully")
    return clf

# Use the trained model to detect jamming patterns in signals
def detect_jamming_pattern(clf, signal):
    prediction = clf.predict([signal])
    if prediction[0] == 1:
        logging.warning("Jamming Pattern Detected by Machine Learning Model")
        print("Jamming Pattern Detected by Machine Learning Model")
        return True
    return False

# Class to manage redundant communication channels and switch dynamically
class CommunicationChannel:
    def __init__(self):
        self.channels = [1, 2, 3, 4, 5]
        self.current_channel = random.choice(self.channels)
        logging.info(f"Initial communication channel set to: {self.current_channel}")
        print(f"Initial communication channel set to: {self.current_channel}")

    def switch_channel(self):
        available_channels = [ch for ch in self.channels if ch != self.current_channel]
        self.current_channel = random.choice(available_channels)
        logging.info(f"Switched to Channel {self.current_channel} due to interference.")
        print(f"Switched to Channel {self.current_channel} due to interference.")

    # Implement frequency hopping to prevent jamming
    def frequency_hopping(self):
        new_channel = random.choice(self.channels)
        while new_channel == self.current_channel:
            new_channel = random.choice(self.channels)
        self.current_channel = new_channel
        logging.info(f"Frequency hopping: Switched to Channel {self.current_channel}")
        print(f"Frequency hopping: Switched to Channel {self.current_channel}")

    # Strategy to recover from jamming: Retry or switch to backup communication protocol
    def recovery_strategy(self):
        print("Jamming detected. Attempting recovery...")
        # Retry by switching to a random available channel or using alternate protocol
        self.switch_channel()
        # Here you can add alternate communication protocols or retry mechanisms
        logging.info("Recovery initiated: Switched to a new channel.")

# Set up encryption for secure communication
def setup_encryption():
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    logging.info("Encryption Cipher Initialized")
    print("Encryption Cipher Initialized")
    return cipher_suite

# Encrypt and decrypt messages for secure transmission
def encrypt_message(cipher_suite, message):
    encrypted_message = cipher_suite.encrypt(message.encode())
    logging.info("Message encrypted for secure transmission")
    print("Message encrypted for secure transmission")
    return encrypted_message

def decrypt_message(cipher_suite, encrypted_message):
    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    logging.info("Message decrypted successfully")
    print("Message decrypted successfully")
    return decrypted_message

# Main Controller for Anti-Jamming Operations
class JamResistanceController:
    def __init__(self):
        self.channel = CommunicationChannel()
        self.detector = train_jamming_detector()
        self.encryption = setup_encryption()

    def monitor_and_respond(self, signal):
        # Detect anomaly
        anomaly_detected, max_amplitude = detect_anomaly(signal)
        
        if anomaly_detected:
            self.channel.switch_channel()

        # Detect jamming pattern using machine learning
        if detect_jamming_pattern(self.detector, signal):
            self.channel.switch_channel()

        # Implement frequency hopping when jamming is detected
        self.channel.frequency_hopping()

        # Implement recovery strategy
        self.channel.recovery_strategy()

        # Encrypt the message
        message = "Drone communication secured."
        encrypted_message = encrypt_message(self.encryption, message)
        decrypt_message(self.encryption, encrypted_message)

        return max_amplitude

# Function to plot signal and its FFT for visualization
def plot_signal_and_spectrum(signal):
    time_points = np.linspace(0, 1, len(signal))
    fft_values = np.abs(fft(signal))
    frequencies = np.fft.fftfreq(len(signal), d=(time_points[1] - time_points[0]))

    # Plot time domain
    plt.figure(figsize=(14, 6))
    plt.subplot(1, 2, 1)
    plt.plot(time_points, signal)
    plt.title("Time Domain: Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")

    # Plot frequency domain
    plt.subplot(1, 2, 2)
    plt.plot(frequencies[:len(frequencies)//2], fft_values[:len(fft_values)//2])
    plt.title("Frequency Domain: FFT Spectrum")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")

    plt.tight_layout()
    plt.show()

# Function to generate advanced feedback flowchart with quantifiable metrics
def generate_advanced_feedback_flowchart(max_amplitude):
    dot = Digraph(comment='Advanced Jamming Detection Feedback')

    # Add nodes with quantifiable metrics
    dot.node('A', 'Signal Generated')
    dot.node('B', f'Anomaly Detected\n(Max Amplitude: {max_amplitude:.2f})')
    dot.node('C', 'Jamming Detected by ML Model')
    dot.node('D', 'Switch Channel')
    dot.node('E', 'Message Encrypted')
    dot.node('F', 'Recovery Initiated\n(Back to Secure Communication)')
    dot.node('G', 'Communication Secured')

    dot.edge('A', 'B', label='Signal Input')
    dot.edge('B', 'C', label='Anomaly Threshold Check')
    dot.edge('C', 'D', label='If Jamming Detected')
    dot.edge('D', 'E', label='Secure Channel Switch')
    dot.edge('E', 'F', label='Recovery Strategy Initiated')
    dot.edge('F', 'G', label='Encryption Success')

    # Render the flowchart with advanced details
    dot.render('advanced_feedback_flowchart_with_recovery', format='png', cleanup=True)

    print("Advanced Feedback flowchart with recovery generated!")
    return 'advanced_feedback_flowchart_with_recovery.png'

# Main Function to Simulate Drone Anti-Jamming System
if __name__ == "__main__":
    controller = JamResistanceController()

    while True:
        try:
            # Request user input for frequency and noise level
            frequency = float(input("\nEnter the signal frequency (Hz, e.g., 50): "))
            noise_level = float(input("Enter the noise level (e.g., 0.1 for low noise, 1.5 for high noise): "))

            # Generate and monitor signal based on user input
            signal = generate_signal(frequency=frequency, noise_level=noise_level)
            print("\nMonitoring new signal...")
            max_amplitude = controller.monitor_and_respond(signal)

            # Ask if the user wants to see the plot
            show_plot = input("Would you like to view the signal plot? (yes/no): ").strip().lower()
            if show_plot == "yes":
                plot_signal_and_spectrum(signal)

            # Ask if the user wants to generate advanced feedback flowchart
            generate_feedback = input("Generate advanced feedback flowchart with recovery details? (yes/no): ").strip().lower()
            if generate_feedback == "yes":
                generate_advanced_feedback_flowchart(max_amplitude)

            # Pause before generating another signal
            time.sleep(2)

        except KeyboardInterrupt:
            print("\nDrone Anti-Jamming System Shutdown")
            break
