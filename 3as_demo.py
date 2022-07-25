import wx
from wxasync import AsyncBind, WxAsyncApp, StartCoroutine
import asyncio
from asyncio.events import get_event_loop
import wx.lib.agw.aui as aui
from collections import defaultdict
import time

import wx.lib.newevent
SomeNewEvent, EVT_SOME_NEW_EVENT = wx.lib.newevent.NewEvent()
SomeNewEventAsync, EVT_SOME_NEW_EVENT_ASYNC = wx.lib.newevent.NewEvent()
kwargs={'debug': False,
 'help': False,
 'lame_duck': 0,
 'num_of_params': 2,
 'open': False,
 'params': ('bucket', 'key'),
 'pipeline': 's3\\view',
 'quiet': False,
 'runtime': 'DEV',
 'ui_layout': 'list_s3_objects_sortable_paginated_sqlite',
 'yes': False}
import cli_layer.config.app_config as app_config  
if 1:
    app_config.init(**kwargs)
    apc = app_config.apc
    apc.validate().load() 
if 1:
    from ui_layer.app import main_ui
    from ui_layer.common import UI_TMP_DIR, UI_CFG_FN

    import ui_layer.config.ui_config as ui_config 
    ui_config.init(**kwargs)
    import ui_layer.config.ui_layout as ui_layout 
    ui_layout.init(**kwargs)
        
        
class Sortable_ListPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, style=wx.WANTS_CHARS, size=(200,200))
      
        button1 =  wx.Button(self, label="AsyncBind")
        AsyncBind(wx.EVT_BUTTON, self.async_download, button1)
    async def async_download(self, event):
        print ('async_download')
        #await asyncio.sleep(1)
        print ('async_download')
        await asyncio.sleep(1)
        print ('async_download')
        await asyncio.sleep(1)
        print ('async_download')
        await asyncio.sleep(1)
        print ('async_download')
        await asyncio.sleep(1)
        print ('async_download')
        await asyncio.sleep(1)
        print ('async_download')
        await asyncio.sleep(1)
        print ('async_download')
        
        
        
        
class TestFrame(wx.Frame):
    def __init__(self, parent=None):
        super(TestFrame, self).__init__(parent)


        panel=Sortable_ListPanel(self)
        self.mgr = aui.AuiManager()
        self.mgr.SetManagedWindow(self)
        self.allowAuiFloating = False
        self.refs=defaultdict(dict)
        if 0:
            from ui_layer.module.ListCtrl_Frame import ListCtrl_Frame
                
            winname   = 'PipelineList'
            winkey    = r'ui_layer\module\ListCtrl_Frame.py.ListCtrl_Frame'
            win = parent=ListCtrl_Frame(parent=self, name=winname, lineno=0, layout_fn = r'C:\Users\alex_\gh\ui_demo\pipeline\s3\view\ui_layout\list_s3_objects_sortable_paginated_sqlite.json' )
            #self.attachWin(win, winkey,winname)

            self.mgr.AddPane(win,aui.AuiPaneInfo().Center().Layer(1).
            BestSize(wx.Size(200,150)).MinSize(wx.Size(200,150)).Caption("PipelineList").
            CloseButton(False).Name("PipelineList").CaptionVisible(False))
        
            self.mgr.Update()
        #self.SetSizer(vbox)
        #self.Layout()
        self.clock_on = False


    def detachWin(self, winkey, winname):
        mgr=self.mgr
        ref= self.refs[winkey][winname]
        pane= mgr.GetPane(ref)
        
        if pane.IsOk():
            pane.Show(False)
            mgr.DetachPane(ref)

        if 1: 
            ref.Show(False)

    def attachWin(self,win, winkey,winname):
        
        if winkey not in self.refs:  self.refs[winkey] = {}
        
        if 1:
            if winname not in self.refs[winkey] :
                self.refs[winkey][winname] = win
            else: 
                win = self.refs[winkey][winname]
                win.Show(True)

    def regular_func_raises_custom_event(self, event):
        print("trigger demo via custom event")
        # Create and post the event
        evt = SomeNewEvent(attr1="hello", attr2=654)
        wx.PostEvent(self, evt)

    def regular_func_raises_custom_async_event(self, event):
        print("trigger async demo via custom event")
        # Create and post the event
        evt = SomeNewEventAsync(attr1="hello", attr2=654)
        wx.PostEvent(self, evt)

    def regular_func_starts_coroutine(self, event):
        self.clock_on = not self.clock_on
        if self.clock_on:
            print(f"triggering an async call via StartCoroutine()")
            StartCoroutine(self.update_clock, self)
        else:
            print("clock flag off, coroutine will stop looping, drop through and complete")

    def on_show_frame(self, event):  # not used
        """manually build a frame with inner html window, no sizer involved"""
        class MyPopupFrame(wx.Frame):
            def __init__(self, parent, title):
                super(MyPopupFrame, self).__init__(parent, title=title)
        frm = MyPopupFrame(parent=self, title="Simple Popup Frame")
        frm.Show()

    def callback(self, event):
        self.edit.SetLabel("Button clicked (synchronous)")
        wx.SafeYield()
        time.sleep(1)
        self.edit.SetLabel("Working (synchronous)")
        wx.SafeYield()
        time.sleep(1)
        self.edit.SetLabel("Completed (synchronous)")
        wx.SafeYield()
        time.sleep(1)
        self.edit.SetLabel("")

    async def async_callback(self, event):
        print("Button clicked")
        self.edit.SetLabel("Button clicked")
        await asyncio.sleep(1)
        print("Working")
        self.edit.SetLabel("Working")
        await asyncio.sleep(1)
        self.edit.SetLabel("Completed")
        await asyncio.sleep(1)
        self.edit.SetLabel("")

    async def update_clock(self):
        while self.clock_on:
            self.edit_timer.SetLabel(time.strftime('%H:%M:%S'))
            await asyncio.sleep(0.5)
        self.edit_timer.SetLabel("")

app = WxAsyncApp()
frame = TestFrame()
frame.Show()
app.SetTopWindow(frame)
loop = get_event_loop()
loop.run_until_complete(app.MainLoop())