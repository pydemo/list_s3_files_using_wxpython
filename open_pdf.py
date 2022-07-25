import wx
from wx.lib.scrolledpanel import ScrolledPanel 
import threading, subprocess
import os

class GUI(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Hey, a GUI!', size=(300,300))
        self.panel = ScrolledPanel(parent=self, id=-1) 
        self.panel.SetupScrolling()  
        self.Bind(wx.EVT_CLOSE, self.OnClose)

        self.openFiles = []

        self.openBtn = wx.Button(self.panel, -1, "Open a File")
        self.pollBtn = wx.Button(self.panel, -1, "Poll")
        self.Bind(wx.EVT_BUTTON, self.OnOpen, self.openBtn)
        self.Bind(wx.EVT_BUTTON, self.OnPoll, self.pollBtn)

        vbox = wx.BoxSizer(wx.VERTICAL)

        vbox.Add((20,20), 1)
        vbox.Add(self.openBtn)
        vbox.Add((20,20), 1)
        vbox.Add(self.pollBtn)
        vbox.Add((20,20), 1)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(vbox, flag=wx.TOP|wx.BOTTOM|wx.LEFT|wx.RIGHT|wx.EXPAND, border = 10)

        self.panel.SetSizer(hbox)
        self.panel.Layout()

    def OnOpen(self, event):
        fileName = "20263789_TRF_1.pdf"
        self.openFiles.append(FileThread(fileName))

    def OnPoll(self, event):
        self.openFiles[0].Poll()

    def OnClose(self, event):
        for file in self.openFiles:
            file.end()
            self.openFiles.remove(file)

        self.Destroy()

class FileThread(threading.Thread):
    def __init__(self, file):
        threading.Thread.__init__(self)
        self.file = file
        self.start()

    def run(self):
        self.doc =doc= subprocess.Popen(["start", " /MAX", "/WAIT", self.file], shell=True)
        return doc

    def Poll(self):
        print ("polling")
        print (self.doc.poll())
        doc=self.doc
        #print(psutil.Process(doc.pid).get_children()[0].kill())
        print (self.doc.pid)

    def end(self):
        try:
            print ("killing file {}".format(self.file))
        except:
            print ("file has already been killed")

def main():
    app = wx.PySimpleApp()
    gui = GUI()
    gui.Show()
    app.MainLoop()


if __name__ == "__main__": main()