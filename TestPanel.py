import wx
from wxasync import AsyncBind, WxAsyncApp, StartCoroutine
import asyncio
from asyncio.events import get_event_loop
import time
import wx.lib.newevent
SomeNewEvent, EVT_SOME_NEW_EVENT = wx.lib.newevent.NewEvent()
SomeNewEventAsync, EVT_SOME_NEW_EVENT_ASYNC = wx.lib.newevent.NewEvent()
class TestPanel(wx.Panel):
    def __init__(self, parent=None):
        super(TestPanel, self).__init__(parent)
        vbox = wx.BoxSizer(wx.VERTICAL)
        button1 =  wx.Button(self, label="AsyncBind (original wxasync example)")
        button11 =  wx.Button(self, label="AsyncBind")
        button2 =  wx.Button(self, label="Start/stop clock via StartCoroutine()")
        button3 =  wx.Button(self, label="Emit Custom Event (sync)")
        button4 =  wx.Button(self, label="Emit Custom Event (async)")
        button5 =  wx.Button(self, label="Show Frame")
        self.edit =  wx.StaticText(self, style=wx.ALIGN_CENTRE_HORIZONTAL|wx.ST_NO_AUTORESIZE)
        self.edit_timer =  wx.StaticText(self, style=wx.ALIGN_CENTRE_HORIZONTAL|wx.ST_NO_AUTORESIZE)
        vbox.Add(button1, 2, wx.EXPAND|wx.ALL)
        vbox.Add(button11, 2, wx.EXPAND|wx.ALL)
        vbox.Add(button2, 2, wx.EXPAND|wx.ALL)
        vbox.Add(button3, 2, wx.EXPAND|wx.ALL)
        vbox.Add(button4, 2, wx.EXPAND|wx.ALL)
        vbox.Add(button5, 2, wx.EXPAND|wx.ALL)
        vbox.AddStretchSpacer(1)
        vbox.Add(self.edit, 1, wx.EXPAND|wx.ALL)
        vbox.Add(self.edit_timer, 1, wx.EXPAND|wx.ALL)
        self.SetSizer(vbox)
        self.Layout()
        self.clock_on = False


        """Binding of button event to async method"""
        AsyncBind(wx.EVT_BUTTON, self.async_callback, button1)
        """Binding of button event to async method"""
        AsyncBind(wx.EVT_BUTTON, self.async_test, button11)
        """
        Regular method calls StartCoroutine()
        No need for async/await syntax except on the final async method! Turtle avoidance success 
        because no need for async/await syntax turtles all the way up the calling chain.
        """
        self.Bind(wx.EVT_BUTTON, self.regular_func_starts_coroutine, button2)

        """
        Synchronous method broadcast a custom event - works ok 
        But this is the synchronous version.  Its the async version we want to get working.
        """
        self.Bind(wx.EVT_BUTTON, self.regular_func_raises_custom_event, button3)
        self.Bind(EVT_SOME_NEW_EVENT, self.callback)  # bind custom event to synchronous handler - works OK

        """
        Bind button to run regular synchronous code, which raises an event
        Bind custom event to asynchronous handler
        """
        self.Bind(wx.EVT_BUTTON, self.regular_func_raises_custom_async_event, button4)
        AsyncBind(EVT_SOME_NEW_EVENT_ASYNC, self.async_callback, self)  # don't specify id

        """Show popup frame"""
        self.Bind(wx.EVT_BUTTON, self.on_show_frame, button5)
    async def async_test(self, event):
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
        await asyncio.sleep(1)
        print ('async_download')
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