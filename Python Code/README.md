# Project Python Code

All code used is contained here.
This includes "libraries" provided for the RPi Stepper Motor HAT used in the project.

"ServoInputTest.py" is the only file written by myself. It builds upon the "ServoTest.py" given and takes keyboard strokes
as input and sets servos to minimum, middle or maximum positions. 4 servos can be connected at any time to 4 channels on
the HAT, Channels 0, 1, 14 and 15. Each servo must be calibrated, since individual servos may be different.
Use with caution, as overloading the servos or attempting to load/drive multiple servos at once may lead to overheating or
board/power failure.
