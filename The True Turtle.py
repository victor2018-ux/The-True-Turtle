import turtle
import keyboard
import time


t = turtle.Turtle()
screen = turtle.Screen()

screen.title("The True Turtle")

while True:
    if keyboard.is_pressed('Up'):
        t.forward(35)
        time.sleep(0.05)
    
    if keyboard.is_pressed('Left'):
        t.left(90)
        time.sleep(0.05)
    
    if keyboard.is_pressed('Right'):
        t.right(90)
        time.sleep(0.05)
        
    if keyboard.is_pressed('Down'):
        t.forward(-35)
        time.sleep(0.05)
        
    if keyboard.is_pressed('R'):
        t.reset()
        time.sleep(0.05)
    
    time.sleep(0.01)