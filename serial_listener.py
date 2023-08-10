import serial
import socket

# Configuration
SERIAL_PORT = 'COM3'  # Adjust this for your system. On Linux, it might be something like '/dev/ttyUSB0'.
BAUDRATE = 9600
IP_ADDRESS = '127.0.0.1'
PORT = 12345

def main():
    # Open serial connection
    ser = serial.Serial(SERIAL_PORT, BAUDRATE)

    # Create socket and connect to server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((IP_ADDRESS, PORT))

    try:
        while True:
            # Read from serial port
            data = ser.readline()

            # Print data
            print(data.decode('utf-8').strip())
            
            # Forward to IP
            client_socket.send(data)
    except KeyboardInterrupt:
        print("Terminating...")
    finally:
        ser.close()
        client_socket.close()

if __name__ == '__main__':
    main()
