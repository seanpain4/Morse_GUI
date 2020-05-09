from Tkinter import *
import tkFont
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)
GPIO.output(13, GPIO.LOW)

win = Tk()
myFont = tkFont.Font(family = 'Helvetica', size = 36, weight = 'bold')
morseCodeDict = { 'A':'.-', 'B':'-...', 
                  'C':'-.-.', 'D':'-..', 'E':'.', 
                  'F':'..-.', 'G':'--.', 'H':'....', 
                  'I':'..', 'J':'.---', 'K':'-.-', 
                  'L':'.-..', 'M':'--', 'N':'-.', 
                  'O':'---', 'P':'.--.', 'Q':'--.-', 
                  'R':'.-.', 'S':'...', 'T':'-', 
                  'U':'..-', 'V':'...-', 'W':'.--', 
                  'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                  '1':'.----', '2':'..---', '3':'...--', 
                  '4':'....-', '5':'.....', '6':'-....', 
                  '7':'--...', '8':'---..', '9':'----.', 
                  '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                  '?':'..--..', '/':'-..-.', '-':'-....-', 
                  '(':'-.--.', ')':'-.--.-'} 


def textToMorseCode():
	morseCodeOutput = []
	print("Converting to Morse Code...")
	inputChars = list(mainInput.get())
	
	for char in inputChars:
		morseCodeOutput.append(morseCodeDict[char.upper()])
	
	morseCodeToLed(morseCodeOutput)
	
	
def morseCodeToLed(inputMorseCode):
	print("Flashing Morse Code...")
	
	for item in inputMorseCode:
		for pulse in item:
			if pulse == ".":
				GPIO.output(13, GPIO.HIGH)
				time.sleep(0.1)
				GPIO.output(13, GPIO.LOW)
			elif pulse == "-":
				GPIO.output(13, GPIO.HIGH)
				time.sleep(0.3)
				GPIO.output(13, GPIO.LOW)
			time.sleep(0.1)
		time.sleep(0.3)
	
	
def mainInputLimit(*args):
    value = mainInputValue.get()
    if len(value) > 12: mainInputValue.set(value[:12])
    

def quitProgram():
	print("Program has been closed.")	
	GPIO.cleanup()
	win.quit()


win.title("LED GUI")
win.geometry('500x400')

mainInputValue = StringVar()
mainInputValue.trace('w', mainInputLimit)

mainLabel = Label(win, text = "Please enter a word to convert to Morse Code!")
mainInput = Entry(win, font = myFont, width = 12, textvariable=mainInputValue)
quitButton = Button(win, text = "Quit", font = myFont, command = quitProgram, height = 1, width = 6)
runButton = Button(win, text = "Run", font = myFont, command = textToMorseCode, height = 1, width = 6)

mainLabel.pack(side = TOP, pady = 20)
mainInput.pack(side = TOP, pady = 10)
quitButton.pack(side = BOTTOM, pady = 20)
runButton.pack(side = BOTTOM, pady = 20)

mainInput.focus()

win.mainloop()
