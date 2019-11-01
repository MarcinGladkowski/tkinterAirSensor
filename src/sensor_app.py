from sensor_api import ApiSensorClient
from tkinter import *
from PIL import ImageTk, Image

class App:
    def __init__(self, root, api_client):
        self.root = root
        self.api_client = api_client
        self.root.geometry("485x320")
        self.root.title("Air quality measure")

        self.img = ImageTk.PhotoImage(Image.open("../images/app_background.jpg"))
        self.image = Label(root, image=self.img)
        self.image.place(x=0, y=0, relwidth=1, relheight=1)

        self.tempLabel = Label(root)
        self.tempLabel.config(font=("Courier", 20))
        self.tempLabel.place(x=20, y=20)


        self.humiLabel = Label(root)
        self.humiLabel.config(font=("Courier", 20))
        self.humiLabel.place(x=20, y=60)

        self.pm2 = Label(root)
        self.pm2.config(font=("Courier", 20))
        self.pm2.place(x=20, y=100)

        self.pm10 = Label(root)
        self.pm10.config(font=("Courier", 20))
        self.pm10.place(x=20, y=140)

        self.root.after(0, self.update_measure)

    def update_measure(self, *args):

        result = self.get_measure_from_api()

        print (result)

        self.tempLabel.update()
        self.tempLabel.config(text="Temperatura: " + str(result["temp"]))

        self.humiLabel.update()
        self.humiLabel.config(text="Wilgotność: " + str(result["humi"]))

        self.pm2.update()
        self.pm2.config(text="PM2: " + str(result["p2"]))

        self.pm10.update()
        self.pm10.config(text="PM10: " + str(result["p1"]))

        root.after(2000, self.update_measure)

    def get_measure_from_api(self):
        return self.api_client.get_measure(self.api_client)



apiClient = ApiSensorClient
root = Tk()
root.attributes("-fullscreen", True)
App(root, apiClient)
root.mainloop()