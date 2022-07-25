#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
"""Sorted ListCtrl"""

import wx
import wx.lib.mixins.listctrl as listmix
import datetime
import sys

#wx.SetDefaultPyEncoding("iso-8859-15")


class SortedListCtrl(wx.ListCtrl, listmix.ColumnSorterMixin):
    
    def __init__(self, parent):
        wx.ListCtrl.__init__(self, parent, style = wx.LC_REPORT)
        
        # Daten mit ID (sortierbare Rohdaten -- keine Strings)
        self.data = {
            0: ("A", 1, datetime.date(2000, 10, 15)),
            1: ("X", 50, datetime.date(1960, 1, 5)),
            2: ("B", 599, datetime.date(3020, 5, 1)),
            3: ("U", 5, datetime.date(1970, 11, 30)),
            4: ("I", 8, datetime.date(2007, 6, 20)),
        }
        self.itemDataMap = self.data
        
        # Spaltenüberschriften
        maxint=9999999
        self.InsertColumn(maxint, "Buchstabe")
        self.InsertColumn(maxint, "Zahl")
        self.InsertColumn(maxint, "Datum")
        
        # Daten in ListCtrl schreiben
        for key in sorted(self.data.keys()):
            char_value, number_value, date_value = self.data[key]
            index = self.InsertStringItem(maxint, char_value)
            self.SetItemData(index, key) #muss sein
            self.SetStringItem(index, 1, str(number_value))
            self.SetStringItem(index, 2, date_value.strftime("%d.%m.%Y"))
            self.SetColumnWidth(2, wx.LIST_AUTOSIZE)
        
        listmix.ColumnSorterMixin.__init__(self, numColumns = 3)
    
    
    def GetListCtrl(self):
        return self
    

class MyFrame(wx.Frame):
    
    def __init__(
        self, parent = None, title = "Example", size = wx.Size(550, 420)
    ):
        wx.Frame.__init__(self, parent, -1, title, size = size)
        
        panel = wx.Panel(self)
        
        vbox_main = wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(vbox_main)
        
        my_list = SortedListCtrl(panel)
        vbox_main.Add(my_list, 1, wx.EXPAND | wx.ALL, 10)


def main():
    """Testing"""
    app = wx.PySimpleApp()
    f = MyFrame()
    f.Center()
    f.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()