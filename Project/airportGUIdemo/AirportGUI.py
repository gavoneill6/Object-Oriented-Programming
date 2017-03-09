from AirportAtlas import AirportAtlas
from tkinter import *

class AirportGUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        parent.geometry("500x200")
        parent.title("Airports")
        self.atlas = AirportAtlas()

        self.codelabel = StringVar()
        self.inputAirportCode = StringVar()
        self.inputAirportCode.trace("w", self.validate)

        self.predictionslabel = StringVar()
        self.airportnamelabel = StringVar()
        self.countrylabel = StringVar()
        self.makecontrols()
        self.pack(fill="y", expand=True)

    def validate(self, name, index, mode): # or just self, *dummy
        self.predictionslabel.set(self.inputAirportCode.get())
        predictions=self.atlas.getAirportPredictions(self.inputAirportCode.get())
        print(predictions)
        self.listbox.delete(0,END)
        for airportname in predictions:
            self.listbox.insert(END, airportname)



    def makecontrols(self):

        controlframe = Frame(self)

        Entry(controlframe, width=5, textvariable=self.inputAirportCode).pack(side="left")
        Button(controlframe, width=10, text="Search",
               command=self.search).pack(side="left")

        self.listbox = Listbox(root)
        self.listbox.pack(side="right")

        Label(self, textvariable=self.codelabel,
              font=("Helvetica", 14)).pack()
        Label(self, textvariable=self.airportnamelabel,
              font=("Helvetica", 12)).pack()
        Label(self, textvariable=self.countrylabel,
              font=("Helvetica", 12)).pack()
        Label(self, textvariable=self.predictionslabel,
              font=("Helvetica", 14)).pack()

        controlframe.pack()

    def search(self):
        print('Searching for airport code:'+ str(self.inputAirportCode.get()))
        myAirport = self.atlas.getAirport(self.inputAirportCode.get())
        print(myAirport)
        self.updatesearch(myAirport)

    def updatesearch(self, myAirport):
        self.codelabel.set(myAirport.code)
        self.airportnamelabel.set(myAirport.name)
        self.countrylabel.set(myAirport.country)

    def callback(self):
        print(self.codelabel.get())

root = Tk()
app = AirportGUI(root)
root.mainloop()
