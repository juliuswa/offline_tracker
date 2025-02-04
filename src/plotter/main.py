import serial 
import time 
import tkinter as tk   
import cv2
from state_machine import StateMachine

LED_HIGH = 400.0
AMPERE_HIGH = 516.0
AMPERE_LOW = 514.0

arduino = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=.1) 

video_paths = {
    "offline": "videos/offline/Offline Intro V1.mp4",
    "online": "videos/offline/Back Online V2.mp4",
}

current_state = "offline"
cap = cv2.VideoCapture(video_paths[current_state])

if not cap.isOpened():
    print(f"Error: Could not open {video_paths[current_state]}")
    exit(1)

cv2.namedWindow("Video Window")

state_machine = StateMachine()
last_ampere = "H"

while True: 
    ret, frame = cap.read()
    if not ret:
        # If the video has ended, loop it (or you could choose to change state here)
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    cv2.imshow("Video Window", frame)
    key = cv2.waitKey(30) & 0xFF
    if key == ord('q'):
        break

    value = arduino.readline().decode("utf-8")
    print(value)

    split_string = value.split(",")

    if len(split_string) != 3:
        print("not 3 values")
        continue

    ampere = float(split_string[0])
    red_led = float(split_string[1])
    green_led = float(split_string[2])
    
    signal = ""

    if ampere > AMPERE_HIGH: 
        signal += "H"
        last_ampere = "H"
    elif ampere < AMPERE_LOW:
        signal += "L"
        last_ampere = "L"
    else:
        signal = last_ampere

    if green_led > LED_HIGH: 
        signal += "G"
    else:
        signal += "R"

    print(signal)
    state_machine.transition(signal)
    print(state_machine.get_current_state())

    new_state = ""
    if (state_machine.current_state == 0 or state_machine.current_state  == 3):
        new_state = "online"
    
    else :
        new_state = "offline"

    if new_state == current_state :
        continue

    current_state = new_state
        
    cap.release()
    video_path = video_paths[current_state]
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error: Could not open {video_path}")
        break

cap.release()
cv2.destroyAllWindows()
    
