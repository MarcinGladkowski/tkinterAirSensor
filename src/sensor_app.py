from sensor_api import ApiSensorClient
from tkinter import *
from PIL import ImageTk, Image

class App:
    def __init__(self, root, api_client):
        self.root = root
        self.api_client = api_client
        self.root.geometry("485x320")
        self.root.title("Air quality measure")

        self.backgroundImage = ImageTk.PhotoImage(Image.open("../images/app_background.jpg"))
        self.backgroundImageYellow = ImageTk.PhotoImage(Image.open("../images/app_background_yellow.jpg"))

        self.canvas = Canvas(root)
        self.canvas.pack(side='top', fill='both', expand='yes')
        self.mainBackground =self.canvas.create_image(0, 0, image=self.backgroundImage, anchor='nw')

        self.tempText = None
        self.humiText = None
        self.pm1Text = None
        self.pm2Text = None

        self.create_sensor_text_elements()

        self.root.after(0, self.update_measure)

    def update_measure(self, *args):

        result = self.get_measure_from_api()

        self.canvas.itemconfigure(self.tempText, text=str("Temperatura: " + str(result["temp"])) + " st.C")
        self.canvas.itemconfigure(self.humiText, text=str("Wilgotność: " + str(result["humi"])) + ' %')
        self.canvas.itemconfigure(self.pm2Text, text=str("PM2.5: " + str(result["p2"])) + ' µg/m³')
        self.canvas.itemconfigure(self.pm1Text, text=str("PM10: " + str(result["p1"])) + ' µg/m³')


        print (result)

        root.after(2000, self.update_measure)

    def get_measure_from_api(self):
        return self.api_client.get_measure(self.api_client)


    def create_sensor_text_elements(self):
        self.tempText = self.canvas.create_text(15, 20, text="Temperatura: ", fill="black", font="Courier 20", anchor='nw')
        self.humiText = self.canvas.create_text(15, 60, text="Wilgotność: ", fill="black", font="Courier 20", anchor='nw')
        self.pm2Text = self.canvas.create_text(15, 100, text="PM2.5: ", fill="black", font="Courier 20", anchor='nw')
        self.pm1Text = self.canvas.create_text(15, 140, text="PM1: ", fill="black", font="Courier 20", anchor='nw')



apiClient = ApiSensorClient
root = Tk()
root.attributes("-fullscreen", True)
App(root, apiClient)
root.mainloop()