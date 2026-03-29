from PyQt5.QtWidgets import *
import sys, json, os, re

class MainWindow(QMainWindow) :
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 150, 480, 400)
        self.config = configRead() #get config )
        self.ui_init() #initilazing ui \ (^_^) /
    
    def ui_init(self) :
        #its so scary ;(
        for objects in self.config :
            if re.search(r"_button$", objects) :
                sample_obj = QPushButton(self.config[objects]["text"], self)

            '''
            elif re.search(r"_label$", objects) :
                sample_obj = QLabel(self)
                sample_obj.text(self.config[objects]["text"])
            '''

            sample_obj.setGeometry(
                self.config[objects]["posx"],
                self.config[objects]["posy"],
                self.config[objects]["sizew"],
                self.config[objects]["sizeh"]
            )

            setattr(self, f"obj_{objects}", sample_obj)

            print(f"object - initilazing {objects}")

            #I'm lazy, guys, sooooo... I DONT MAKE COMMENTS :b


def main() :
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

#reading config ^^
def configRead() :
    try :
        #trying read config "config.json" in main file dir )
        with open("config.json", "r") as json_config :
            config = json.load(json_config) #loding config.json in config

        #if all ready pinting text
        print(config)
        print("config - get")
    except FileNotFoundError :
        #elif file not found (
        print("error - config file not found\ncreat - new config file")

        #writing file
        with open("config.json", "w") as json_config :
            json_config.write() #creat null json file
    
    return config

if __name__ == '__main__' :
    main()