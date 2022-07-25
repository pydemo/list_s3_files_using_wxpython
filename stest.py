import wx
import wx.lib.mixins.listctrl as listmix
from wx.lib.agw import ultimatelistctrl as ULC

APPNAME='Sortable Ultimate List Ctrl'
APPVERSION='1.0'
MAIN_WIDTH=300
MAIN_HEIGHT=300
class TestUltimateListCtrlPanel(wx.Panel, listmix.ColumnSorterMixin):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, style=wx.WANTS_CHARS, size=(MAIN_WIDTH,MAIN_HEIGHT))

        self.list_ctrl = ULC.UltimateListCtrl(self, -1, agwStyle=ULC.ULC_REPORT|ULC.ULC_HAS_VARIABLE_ROW_HEIGHT)
        self.list_ctrl.InsertColumn(0, "Make")
        self.list_ctrl.InsertColumn(1, "Model")
        self.list_ctrl.InsertColumn(2, "Year")
        self.list_ctrl.InsertColumn(3, "Color")

        rows = [("Ford", "Taurus", "1996", "Blue"),
                ("Nissan", "370Z", "2010", "Green"),
                ("Porche", "911", "2009", "Red")
                ]

        for rowIndex, data in enumerate(rows):
            for colIndex, coldata in enumerate(data):
                if colIndex == 0:
                    self.list_ctrl.InsertStringItem(rowIndex, coldata)
                else:
                    self.list_ctrl.SetStringItem(rowIndex, colIndex, coldata)
            self.list_ctrl.SetItemData(rowIndex, data)

        self.itemDataMap = {data : data for data in rows} 

        listmix.ColumnSorterMixin.__init__(self, 4)
        self.Bind(wx.EVT_LIST_COL_CLICK, self.OnColClick, self.list_ctrl)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.list_ctrl, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(sizer)

    def GetListCtrl(self):
        return self.list_ctrl

    def OnColClick(self, event):
        pass
class MyForm(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,wx.ID_ANY,'%s v%s' % (APPNAME,APPVERSION),size=(MAIN_WIDTH,MAIN_HEIGHT),style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN)
        panel = TestUltimateListCtrlPanel(self)

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()