import serial 
import time 
import tkinter as tk   
import cv2

LED_HIGH = 400.0
AMPERE_HIGH = 150.0

arduino = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=.1) 

# 0: kein phone
# 1: phone abgelegt
# 2: phone da
# 3: phone weggenommen

state = 0

state_transitions = {
    0: {
        "HG" : 2,
        "HR" : 0,
        "LG" : 1,
        "LR" : 0
    },
    1: {
        "HG" : 2,
        "HR" : 0,
        "LG" : 1,
        "LR" : 0
    },
    2: {
        "HG" : 2,
        "HR" : 0,
        "LG" : 3,
        "LR" : 0
    },
    3: {
        "HG" : 2,
        "HR" : 0,
        "LG" : 3,
        "LR" : 0
    }
}

video_paths = {
    "intro": "videos/offline/Offline Intro V1.mp4",
    "online": "videos/offline/Back Online.mp4",
}

current_state = "intro"
cap = cv2.VideoCapture(video_paths[current_state])

if not cap.isOpened():
    print(f"Error: Could not open {video_paths[current_state]}")
    exit(1)

cv2.namedWindow("Video Window")

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
    else:
        signal += "L"

    if green_led > LED_HIGH: 
        signal += "G"
    else:
        signal += "R"

    state = state_transitions[state][signal]
    
    if state == 0:
        print("kein handy")
    elif state == 1:
        print("handy gelegt")
    elif state == 2:
        print("handy da")
    elif state == 3:
        print("handy genommen")

    new_state = ""
    if (state == 0 or state == 3):
        new_state = "online"
    
    else :
        new_state = "intro"

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
    
