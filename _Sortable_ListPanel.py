import wx
from wxasync import AsyncBind, WxAsyncApp, StartCoroutine
class _Sortable_ListPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, style=wx.WANTS_CHARS, size=(200,200))
      
        button1 =  wx.Button(self, label="AsyncBind")
        AsyncBind(wx.EVT_BUTTON, self.async_download, button1)
    async def async_download(self, event):
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
        
        