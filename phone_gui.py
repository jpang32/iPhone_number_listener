import tkinter as tk
import time

class PhoneGui:

    def __init__(self, title):

        self.parent = tk.Tk()
        self.parent.title(title)
        self.parent.geometry('300x400')
        #self.parent.config(bg='#5f734c')

        self.canvas = tk.Canvas(self.parent, width=300, height=400)
        self.canvas.pack()
        # x: 75, 150, 225
        # y: 80, 160, 240, 320
        self.num_to_coords = {}
        self.num_to_coords[1] = [50, 55, 100, 105]
        self.num_to_coords[2] = [125, 55, 175, 105]
        self.num_to_coords[3] = [200, 55, 250, 105]

        self.num_to_coords[4] = [50, 135, 100, 185]
        self.num_to_coords[5] = [125, 135, 175, 185]
        self.num_to_coords[6] = [200, 135, 250, 185]

        self.num_to_coords[7] = [50, 215, 100, 265]
        self.num_to_coords[8] = [125, 215, 175, 265]
        self.num_to_coords[9] = [200, 215, 250, 265]

        self.num_to_coords['*'] = [50, 295, 100, 345]
        self.num_to_coords[0] = [125, 295, 175, 345]
        self.num_to_coords['#'] = [200, 295, 250, 345]

        for key in self.num_to_coords:
            self._draw_circle(self.num_to_coords[key])

    def _draw_circle(self, coords, color=''):

        self.canvas.create_oval(coords[0], coords[1], coords[2], coords[3], fill=color)


    def update(self, nums):

        for value in nums:
            self._draw_circle(self.num_to_coords[value], color='blue')
            self.parent.update()
            time.sleep(0.5)
            self._draw_circle(self.num_to_coords[value], color='white')
            self.parent.update()


