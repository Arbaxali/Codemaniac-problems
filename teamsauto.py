# import pyautogui
# import time
# import PySimpleGUI as sg
# from  threading import *
# # Define the GUI layout

# def threading(stopp):
#     t1 = Thread(target=mainn)
#     t1.start()
#     if stopp == True:
#         t1.join()




# def mainn():
#     try:
#         layout = [[sg.Text('Enter the number of clicks to perform: '), sg.InputText()],
#                   [sg.Text('Entert the interval between messages (in seconds): '), sg.InputText()],
#                   [sg.Button('Start'), sg.Button('Stop')]]

#         # Create the GUI window
#         window = sg.Window('Microsoft Teams Clicker', layout)

#         # Run the event loop
#         while True:
#             event, values = window.read()

#             # If the user clicks the 'Start' button
#             if event == 'Start':
#                 # Get the number of clicks and interval between messages
#                 num_clicks = int(values[0])
#                 type_interval = float(values[1])

#                 # wait for 5 seconds before starting the script
#                 time.sleep(5)

#                 # loop through the number of clicks and type a message
#                 for i in range(num_clicks):
#                     # move the mouse to the Teams icon and click it
#                     pyautogui.click()

#                     # wait for Teams to open
#                     time.sleep(10)

#                     # type a message in the chat window
#                     pyautogui.typewrite("Hello, Qiri how are you", interval=5)
#                     pyautogui.press('enter')

#                     # wait for the message to be sent
#                     time.sleep(type_interval)

#                 # wait for 5 seconds before exiting the script
#                 time.sleep(5)

#             # If the user clicks the 'Stop' button
#             if event == 'Stop' or event == sg.WINDOW_CLOSED:
#                 stopp = True
#                 threading(stopp)
#                 break

#     except Exception as e:
#         print(f"An error occurred: {str(e)}")

#     finally:
#         # Close the window and exit the program
#         window.close()



# if __name__ == "__main__":
#     threading()

import pyautogui
import time
import PySimpleGUI as sg
from threading import Thread

# Define the GUI layout
layout = [
    [sg.Text('Enter the number of clicks to perform: '), sg.InputText()],
    [sg.Text('Enter the interval between messages (in seconds): '), sg.InputText()],
    [sg.Button('Start'), sg.Button('Stop')]
]

# Create the GUI window
window = sg.Window('Microsoft Teams Clicker', layout)

# Flag to indicate whether the thread should stop
stop_thread = False

# Function to perform the clicking and typing actions
def perform_actions(num_clicks, type_interval):
    # wait for 5 seconds before starting the script
    time.sleep(5)

    for i in range(num_clicks):
        # Check if the thread should stop
        if stop_thread:
            break

        # move the mouse to the Teams icon and click it
        pyautogui.click()

        # wait for Teams to open
        time.sleep(10)

        # type a message in the chat window
        pyautogui.typewrite("Hello, Qiri how are you", interval=0.1)
        pyautogui.press('enter')

        # wait for the message to be sent
        time.sleep(type_interval)

    # wait for 5 seconds before exiting the script
    time.sleep(5)

# Function to handle the button events
def handle_events():
    while True:
        event, values = window.read()

        if event == 'Start':
            num_clicks = int(values[0])
            type_interval = float(values[1])

            # Create a child thread for performing the actions
            t = Thread(target=perform_actions, args=(num_clicks, type_interval))
            t.start()

        if event == 'Stop' or event == sg.WINDOW_CLOSED:
            # Set the flag to stop the thread
            global stop_thread
            stop_thread = True
            t.join()
            break

    # Close the window and exit the program
    window.close()

# Run the event handling function in the main thread
handle_events()
