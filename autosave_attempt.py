import keyboard 
from threading import Timer

t = Timer(2,'saving')

while True:  # Loop to simulate service
    try:
        if keyboard.is_pressed('a'):
            print('You Pressed A Key!')
            break  # finishing the loop
    except:
        break 
        
        
# Reference Code Exmples

#Reference 1

#from pynput.keyboard import Key, Listener

#def on_press(key):
#    print('{0} pressed'.format(
#        key))

#def on_release(key):
#    print('{0} release'.format(
#        key))
#    if key == Key.esc:
        # Stop listener
#        return False

# Collect events until released
#with Listener(
#        on_press=on_press,
#        on_release=on_release) as listener:
#    listener.join()
#    root.after(1000 * 5, autosave) # time in milliseconds


#Reference 2

#import tkinter
#root = tkinter.Tk()

#def autosave():
    # do something you want
#    print("Hola mundo")
#    root.after(1000 * , autosave) # time in milliseconds
#autosave() 
#root.mainloop()