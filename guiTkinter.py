import Tkinter
import logging
import datetime

module_logger = logging.getLogger(__name__)

class GUI(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent

        self.grid()

        self.IPLabel = Tkinter.Label(self, text="IP").grid(column=0, row=0,sticky='W',padx=10, pady=10)
        self.PortLabel = Tkinter.Label(self, text="PORT").grid(column=0, row=1, sticky='W',padx=10, pady=10)
        self.TokenLabel= Tkinter.Label(self, text="Token").grid(column=3, row=1,sticky='W', padx=10, pady=10)

        self.e1=Tkinter.Entry(self).grid(column=0, row=0, sticky='E',padx=10, pady=10)
        self.e2=Tkinter.Entry(self).grid(column=0, row=1, sticky='E',padx=10, pady=10)
        self.mytext = Tkinter.Text(self, state="disabled",height=1,width=14).grid(column=3, row=1,columnspan=2,padx=10, pady=10)

        self.startbutton = Tkinter.Button(self, text="Start")
        self.startbutton.grid(column=3,row=0,sticky='EW',padx=10, pady=10)
        self.startbutton.bind("<ButtonRelease-1>", self.start_button_callback)

        self.stopbutton = Tkinter.Button(self, text="Stop")
        self.stopbutton.grid(column=4, row=0, sticky='ew',padx=10, pady=10)
        self.stopbutton.bind("<ButtonRelease-1>", self.stop_button_callback)

        self.mytext = Tkinter.Text(self, state="disabled")
        self.mytext.grid(row=2,column=0, columnspan=5)

    def start_button_callback(self, event):
        now = datetime.datetime.now()
        module_logger.info(now)

    def stop_button_callback(self, event):
        now = datetime.datetime.now()
        module_logger.info(now)

class MyHandlerText(logging.StreamHandler):
    def __init__(self, textctrl):
        logging.StreamHandler.__init__(self) # initialize parent
        self.textctrl = textctrl

    def emit(self, record):
        msg = self.format(record)
        self.textctrl.config(state="normal")
        self.textctrl.insert("end", msg + "\n")
        self.flush()
        self.textctrl.config(state="disabled")

if __name__ == "__main__":


    app = GUI(None)
    app.title('CoAP Server')

    stderrHandler = logging.StreamHandler()  # stderr
    module_logger.addHandler(stderrHandler)
    guiHandler = MyHandlerText(app.mytext)
    module_logger.addHandler(guiHandler)
    module_logger.setLevel(logging.INFO)
    module_logger.info("from main")

    # start Tk
    app.mainloop()
