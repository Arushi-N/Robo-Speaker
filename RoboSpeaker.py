import os

if __name__ == "__main__":
    print("Welcome to RoboSpeaker 1.1. Created by Arushi")

    while True:

        x = input("What would you like me to say: ")

        if x=="q":
            os.system("powershell -Command \"Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'bye bye friend\');\"")
            break

        command = f'powershell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{x}\');"'

        os.system(command)
