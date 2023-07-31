import os
if __name__ == '__main__':
    print("Welcome to Robospeaker 1.0 created by Faisal")
    while True :
        x = input("Enter what you want me to pronounce: ")
        if x == 'q':
            break;
        command = f"say {x}"
        os.system(command)
