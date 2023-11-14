import serial
import time
import numpy as np

def arduino():
    # Establish connection (replace 'COM3' with your Arduino's port)
    arduino = serial.Serial('COM3', 9600)
    time.sleep(2)  # Give some time to establish the connection

    # Sending data
    arduino.write(b'Hello Arduino!')
    cnt=0
    # Receiving data
    while True:
        if arduino.in_waiting > 0:
            cnt+=1
            data = arduino.readline().decode().strip()
            #print("Data received:",data)
            if( data[0]=='H'):
                #print("Data needed:",data)
                p=data.split('/')
                #print(p)
                # Find the index of ':'
                index_of_colon = p[0].find(':')
                # Find the index of 'b'
                index_of_b = p[0].find('b')
                # Extract the substring
                pulse = p[0][index_of_colon+1:index_of_b]  # +1 to start after the colon
                #print("pulse",pulse)
                p[0]=pulse

                index_of_colon = p[1].find(':')
                # Find the index of 'b'
                index_of_b = p[1].find('%')
                # Extract the substring
                popct = p[1][index_of_colon+1:index_of_b]  # +1 to start after the colon
                #print("spo2",popct)
                p[1]=popct

                p=np.array(p, dtype=np.float64)
                if(p[0]>0 and p[1]>0):
                    print(p)
                    return p
                #print(p)break
                #np.array(x1, dtype=np.float64)
                
