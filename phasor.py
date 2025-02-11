import matplotlib as mp
import re


class Phasor:
    def __init__(self, name, angle, magnitutde, color):
        self.name = name
        self.angle = angle
        self.magnitude = magnitutde
        self.set_color = color
