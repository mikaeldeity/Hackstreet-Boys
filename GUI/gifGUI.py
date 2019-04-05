
#############-------------\-------------#############

import clr

clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import Application, Form, Label, Button, DockStyle, AnchorStyles, Panel, ComboBox 
from System.Windows.Forms import WebBrowser, LinkLabel, OpenFileDialog, ToolBar, ToolBarButton, TextBox, ScrollBars, PictureBox, FormWindowState, PictureBoxSizeMode, AutoSizeMode
from System.Drawing import Size, Point, Font, Bitmap, Icon, Color

clr.AddReference('RevitAPIUI')
from  Autodesk.Revit.UI import Selection

clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

import sys
pyt_path = r'C:\Program Files (x86)\IronPython 2.7\Lib'
sys.path.append(pyt_path)


import webbrowser

run = IN[0]
url = IN[1]
logo = IN[2] 
icon = IN[3]
image = IN[4]

buttonSpace = 20
panelSpace = 35
cancelSpace = 75


class IForm(Form):
#Create the winfrom UI

    def __init__(self):
        #self is the UI itself


        self.Text = "HACKSTREET BOYS"
        self.output = "false"
        self.Icon = Icon.FromHandle(icon.GetHicon()) #takes a png and converts to a file that can be used as a Icon
        
        #Below commands make sure the window appears in front of all other windows.
        self.WindowState = FormWindowState.Normal
        self.BringToFront()
        self.Topmost = True
        self.Focus()
        self.CenterToScreen()
        self.BackColor = Color.White 

        self.Width = 500
        self.Height = 300    
        width = self.Width
        height = self.Height 

#///////////////////////////////////////////////////////////////////////////////////

        #create winform elements for buttons and links etc
        font = Font("Helvetica ", 9)
        btnOk = Button()
        btnCancel = Button()
        helplink = LinkLabel()
        pic = PictureBox()
        mainPic = PictureBox()
        panel1 = Panel()
        panel = Panel()
        scrollbar = ScrollBars()



#///////////////////////////////////////////////////////////////////////////////////

        #logo file
        pic.Parent = self
        pic.Location = Point(10,height -90)
        ratio = (logo.Height/logo.Width)
        h = float(logo.Height)
        w = float(logo.Width)
        ratio = h/w 
        pic.Size = Size(100,100*ratio) # scale the image byu the ratio of the dif between h & w
        pic.SizeMode = PictureBoxSizeMode.Zoom # zooms the image to fit the picture box extent
        pic.Image = logo
        pic.Anchor = (AnchorStyles.Bottom | AnchorStyles.Left)
        
        
        
        
#///////////////////////////////////////////////////////////////////////////////////

        #logo file
        mainPic.Parent = self
        mainPic.Location = Point(5,5)
        ratio = (logo.Height/logo.Width)
        h = float(logo.Height)
        w = float(logo.Width)
        ratio = h/w 
        mainPic.Size = Size(300,300*ratio) # scale the image byu the ratio of the dif between h & w
        mainPic.SizeMode = PictureBoxSizeMode.Zoom # zooms the image to fit the picture box extent
        mainPic.Image = image
        mainPic.Anchor = (AnchorStyles.Bottom | AnchorStyles.Left)

#///////////////////////////////////////////////////////////////////////////////////

        helplink.Parent = self
        helplink.Text = "User Guide"
        helplink.Tag = url
        helplink.Click += self.openurl
        helplink.Location = Point(width/3, height - 65)
        self.Controls.Add(helplink) #self.Controls create the hyerlink
        helplink.Anchor = (AnchorStyles.Bottom | AnchorStyles.Left)

#///////////////////////////////////////////////////////////////////////////////////

        pHeight = btnOk.Height + panelSpace
        panel1.Height = pHeight
        panel1.Dock = DockStyle.Bottom
        panel1.Parent = self
        #panel is a box within the UI the bottom is hosted to. the panel is hosted to the UI popup itself.

        x = btnOk.Width *2 + buttonSpace
        y = (pHeight - btnOk.Height) / 2

#///////////////////////////////////////////////////////////////////////////////////

        btnOk.Parent = panel1
        btnOk.Text = "Ok"
        btnOk.Location = Point(width-x,y)
        btnOk.Anchor = (AnchorStyles.Right | AnchorStyles.Bottom)
        btnOk.Click += self.okButtonPressed
        #create the putton, host it to the panel. anchor locks it the the UI so it moves with the window if it is scaled.it
        #self.okButtonPressed is the insruction what to do when the button is pressed

        btnCancel.Parent = panel1
        btnCancel.Text = "Cancel"
        btnCancel.Location = Point((width-x + cancelSpace),y)
        btnCancel.Anchor = (AnchorStyles.Right | AnchorStyles.Bottom)
        btnCancel.Click += self.CnlButtonPressed


#///////////////////////////////////////////////////////////////////////////////////



#///////////////////////////////////////////////////////////////////////////////////

        #autosize the form to adjust to textbox
        self.AutoSize = True
        self.AutoSizeMode = AutoSizeMode.GrowAndShrink  



    def okButtonPressed(self, sender, args):
        self.Close()
        self.output = True
        #when ok button pressed close UI and output true


    def CnlButtonPressed(self, sender, args):
        self.Close()
        self.output = False


    def openurl(self, sender, event):
        webbrowser.open(sender.Tag)
        self.Close()
        self.output = True


        

form = IForm()
  
if run == True:

    Application.Run(form)
    results = form.output
    # outputs from the form must be declared as form.xxxx 

    OUT = results

else: 

	OUT = False