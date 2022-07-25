import wx
from wxasync import AsyncBind, WxAsyncApp, StartCoroutine
import asyncio
from asyncio.events import get_event_loop
import time
import wx.lib.agw.aui as aui


import cli_layer.config.app_config as app_config 

if 1:
    app_config.init(**kwargs)
    apc = app_config.apc
    apc.validate().load()
        
        

from TestPanel_3 import TestPanel
class TestFrame(wx.Frame):
    def __init__(self, parent=None):
        super(TestFrame, self).__init__(parent)
        vbox = wx.BoxSizer(wx.VERTICAL)
        panel=TestPanel(self)
        if 1:
            self.mgr = aui.AuiManager()
            self.mgr.SetManagedWindow(self)
            self.allowAuiFloating = False
            #self.refs=defaultdict(dict)
            
            self.mgr.AddPane(panel,aui.AuiPaneInfo().Center().Layer(1).
            BestSize(wx.Size(200,150)).MinSize(wx.Size(200,150)).Caption("PipelineList").
            CloseButton(False).Name("PipelineList").CaptionVisible(False))


app = WxAsyncApp()
frame = TestFrame()
frame.Show()
app.SetTopWindow(frame)
loop = get_event_loop()
loop.run_until_complete(app.MainLoop())