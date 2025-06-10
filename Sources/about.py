import sys
import Frameworks.Logger as Logger
import Frameworks.Utils as Utils
from PIL import Image  

import gc

import maliang
import maliang.animation

class Application:
    def getScaled(self, number: float) -> int:
        return int(number * self.UI_SCALE)

    def __init__(self, args):
        Logger.output('Starting Chrona...')

        self.bus          = args 
        self.IS_DEVMODE   = args.IS_DEVMODE   

        self.UI_SCALE     = args.UI_SCALE     
        self.UI_FPS       = args.UI_FPS       
        self.UI_THEME     = args.UI_THEME 
        self.UI_ANIMATIME = args.UI_ANIMATIME
        self.UI_LOCALE    = args.UI_LOCALE
        self.UI_FAMILY    = args.UI_FAMILY

        self.UI_WIDTH     = self.getScaled(750)
        self.UI_HEIGHT    = self.getScaled(780)
        
        self.utils        = Utils.Utils(self)

        self.loadImage()
        self.createWindow()
        self.loadWidget()

        gc.enable()

        self.root.mainloop()

    def loadImage(self):
        try:
            self.IMG_icon = Image.open('./Resources/icon.png')
        except Exception as e:
            Logger.output(f"Error loading images: {e}", type=Logger.Type.ERROR)
            sys.exit()

    def createWindow(self):
        self.root = maliang.Tk(size=(self.UI_WIDTH, self.UI_HEIGHT))

        self.root.title('Chrona')
        # self.root.icon(maliang.PhotoImage(self.IMG_icon.resize(size=(32, 32), resample=1)))

        self.root.maxsize(self.UI_WIDTH, self.UI_HEIGHT)
        self.root.minsize(self.UI_WIDTH, self.UI_HEIGHT)

        self.cv = maliang.Canvas(self.root)
        self.cv.place(x=0, y=0, width=self.UI_WIDTH, height=self.UI_HEIGHT)
        self.root.center()

        # maliang.Env.system = 'Windows10'

    def loadWidget(self):
        content_start_at = self.getScaled(55)
        # device = maliang.Text(self.cv, position=(content_start_at, self.getScaled(140)), text='Device specifications', family=self.UI_FAMILY, fontsize=self.getScaled(17), weight='bold')

        system_label    = maliang.Label(self.cv, position=(content_start_at, self.getScaled(25)), size=(self.UI_WIDTH - content_start_at * 2, self.getScaled(150)), family=self.UI_FAMILY, fontsize=self.getScaled(17), weight='bold')
        system_icon     = maliang.Image(system_label, anchor='w', position=(self.getScaled(120), system_label.size[1] // 2 + self.getScaled(5)), image=maliang.PhotoImage(self.IMG_icon.resize((self.getScaled(100), self.getScaled(100)), resample=1)))
        system_name     = maliang.Text(system_label, position=(self.getScaled(235), self.getScaled(40)), family=self.UI_FAMILY, text='OmegaOS', fontsize=self.getScaled(25))
        system_desktop  = maliang.Text(system_label, position=(self.getScaled(235), self.getScaled(75)), family=self.UI_FAMILY, text='Desktop Environment', fontsize=self.getScaled(30))
        system_name.style.set(fg=('#BBBBBB'))

        