import re
import matplotlib as mp
import Phasor


class PhasorPlot:
    def __init__(self):
        self.reference_phasor = None
        self.phasor_list = []

    def __get_available_name__(self):
        """
        Find an available phasor name of the format
        'phasor_1', 'phasor_2', 'phasor_3', etc
        """
        name_list = []
        for name in self.phasor_list:
            if name[:6] == "phasor_":
                name_list.add(name)

        phasor_number_max = 0
        for name in name_list:
            phasor_number = int(re.findall(r"\d+", name))
            if phasor_number > phasor_number_max:
                phasor_number_max = phasor_number

        return phasor_number_max

    def set_reference_phasor(self, name):
        """
        Set a phasor to be the reference phasor for the circuit

        This phasor will become the phasor located at 0° and all
        other phasors will have their angle adjusted accordingly
        """
        for item in self.phasor_list:
            if item.name == name:
                self.reference_phasor = item
                break
        raise Exception("Phasor not found in plot!")

    def set_reference_phasor(self, new_reference_phasor):
        """
        Set a phasor to be the reference phasor for the circuit

        This phasor will become the phasor located at 0° and all
        other phasors will have their angle adjusted accordingly
        """
        for item in self.phasor_list:
            if item == new_reference_phasor:
                self.reference_phasor = new_reference_phasor
                break
        raise Exception("Phasor not found in plot!")

    def add_phasor(self, new_phasor):
        """
        Add phasor to the plot.
        """
        self.phasor_list.add(new_phasor)

    def add_phasor(self, angle, magnitude):
        """
        Add phasor to the plot.
        """
        new_phasor = Phasor(self.__get_available_name__(), angle, magnitude, "black")
        self.add_phasor(new_phasor)

    def remove_phasor(self, target_phasor_name):
        """
        Remove phasor from the plot
        """
        for item in self.phasor_list:
            if item.name == target_phasor_name:
                self.remove_phasor(item)

    def remove_phasor(self, target_phasor):
        """
        Remove phasor from the plot
        """
        self.phasor_list.remove(target_phasor)

    def change_color(self, name, new_color):
        """
        Change map color of a specific phasor
        """
        for item in self.phasor_list:
            if item.name == name:
                item.setColor(new_color)

    def draw_phasor_diagram():
        
