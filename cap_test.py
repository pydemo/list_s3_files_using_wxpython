import wx
##import wx.aui as aui
import wx.lib.agw.aui as aui
import wx.lib.agw.ribbon as RB


class Main(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='TITLE_FRAME',size=(wx.DefaultSize),pos=wx.DefaultPosition)
        #self.Centre(wx.BOTH)

        # Create an AUI Manager and tell it to manage this Frame
        self._manager = aui.AuiManager()
        self._manager.SetManagedWindow(self)



        inner_panel3 = wx.Panel(parent=self)
        inner_panel3.SetBackgroundColour('#9999A0')
        inner_panel3.SetMinSize((100, 100))
        inner_panel3_info = aui.AuiPaneInfo().Name('inner_panel3').Caption('Inner Panel 3').CenterPane()


        self._ribbon = RB.RibbonBar(self, wx.ID_ANY)
        self._bitmap_creation_dc = wx.MemoryDC()
        self._colour_data = wx.ColourData()

        self._ribbon.SetArtProvider(RB.RibbonAUIArtProvider())

        # ribbonBar > ribbon page   > ribbon pannel > ribbon toolbar
        #           > examples      > Toolbar       > toolbar 
        home = RB.RibbonPage(self._ribbon, wx.ID_ANY, "Examples", wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN))
        toolbar_panel = RB.RibbonPanel(home, wx.ID_ANY, "Toolbar", wx.NullBitmap, wx.DefaultPosition,
                                       wx.Size(300,300), RB.RIBBON_PANEL_NO_AUTO_MINIMISE)

        toolbar = RB.RibbonToolBar(toolbar_panel, -1)
        # this is just a simple tool
        toolbar.AddTool(wx.ID_ANY,  wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN))
        toolbar.AddTool(wx.ID_ANY, wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN))
        toolbar.AddSeparator()

        sel = RB.RibbonPage(self._ribbon, wx.ID_ANY, "Examples", wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN))

        selection_panel = RB.RibbonPanel(sel, wx.ID_ANY, "Selection", wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN))
        selection = RB.RibbonButtonBar(selection_panel)
        selection.AddSimpleButton(wx.ID_ANY, "Expand Vertically", wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN), "")
        selection.AddSimpleButton(wx.ID_ANY, "Expand Horizontally", wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN), "")
        selection.AddSimpleButton(wx.ID_ANY, "Contract", wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN),"")




        self._ribbon.Realize()

        ribbon_info = aui.AuiPaneInfo().Name('ribbon').Caption('Can I get rid of this gray bar').Top().Floatable(False).CloseButton( visible=False).BestSize(150,150).DockFixed()
        ribbon_info.CaptionVisible(False)


        self._manager.AddPane(inner_panel3, inner_panel3_info)
        self._manager.AddPane(self._ribbon, ribbon_info)

        self._manager.GetPane("ribbon").Layer(0).Row(0).Position(0)     

        self._manager.Update()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = Main()
    frame.Show()
    app.MainLoop()