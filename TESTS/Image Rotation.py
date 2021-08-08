import time
import tkinter
from PIL import Image, ImageTk

class SimpleApp(object):
    def __init__(self, master, filename, **kwargs):
        self.master = master
        self.filename = filename
        self.canvas = tkinter.Canvas(master, width=500, height=500,background="white")
        self.canvas.pack()

        self.process_next_frame = self.draw().__next__  # Using "next(self.draw())" doesn't work
        master.after(1, self.process_next_frame)

    def draw(self):
        image = Image.open(self.filename).convert("RGBA")
        angle = 0
        print(self.process_next_frame)
        while True:
            tkimage = ImageTk.PhotoImage(image.rotate(angle,expand=1))
            canvas_obj = self.canvas.create_image(250, 250, image=tkimage)
            self.master.after_idle(self.process_next_frame)
            yield
            self.canvas.delete(canvas_obj)
            angle += 10
            angle %= 360
            #time.sleep(0.002)

root = tkinter.Tk()
app = SimpleApp(root, '../VERSIONS/v0.1/INTERFACE/GIF/LOADING/Buffer.gif')
root.mainloop()
