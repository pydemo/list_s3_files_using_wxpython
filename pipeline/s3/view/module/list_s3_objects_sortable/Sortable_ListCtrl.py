#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
"""Sorted ListCtrl"""

import wx
import wx.lib.mixins.listctrl as listmix
import datetime
import sys
import wx
import os, sys, time, json
from os.path import isfile, dirname, join, isdir
import subprocess
from pprint import pprint as pp
from ui_layer.log_init import log, info, debug
from ui_layer.Base import reciever


from ui_layer.utils import exception
from pathlib import Path

from ui_layer.common import open_editor
from ui_layer.module.controller.Searcheable_ListCtrl_Controller import Controller


import cli_layer.aws_pipeline_utils  as APU
import cli_layer.s3_utils  as S3U
import ui_layer.config.ui_config as ui_config
uic = ui_config.uic





def get_S3_File_List():
    bucket_name= 'gh-package-pdf'
    bucket_name= 'k9-filestore'
    prefix='k9-feed-doc-lims/'
    pd = S3U.list_s3_files(bucket_name, prefix,MaxItems=1000000, PageSize=1000)
    #header
    #print('source,pipeline_name')
    rows={}
    for pid, ppl in enumerate(sorted(pd)):
        #pp(pd[ppl])
        #e()
        rows[pid] =(pid, f'{bucket_name}/{prefix}',pd[ppl]['Key'].lstrip(prefix),pd[ppl]['Size'])
    header = ['Id', 'Bucket','Key', 'Size']
    print('Got ', len(rows))
    return header, rows
    
class _Sortable_ListCtrl(wx.ListCtrl, listmix.ColumnSorterMixin):
    
    def __init__(self, parent):
        wx.ListCtrl.__init__(self, parent, style = wx.LC_REPORT)
        
        # Daten mit ID (sortierbare Rohdaten -- keine Strings)
        if 0:
            self.data = {
                0: ("A", 1, datetime.date(2000, 10, 15)),
                1: ("X", 50, datetime.date(1960, 1, 5)),
                2: ("B", 599, datetime.date(3020, 5, 1)),
                3: ("U", 5, datetime.date(1970, 11, 30)),
                4: ("I", 8, datetime.date(2007, 6, 20)),
            }
        header, self.data = get_S3_File_List()
        self.itemDataMap = self.data
        
        # Spaltenüberschriften
        maxint=99999999
        for col in header:
            self.InsertColumn(maxint, col)
        #self.InsertColumn(maxint, "Zahl")
        #self.InsertColumn(maxint, "Datum")
        if 0:
            # Daten in ListCtrl schreiben
            for key in sorted(self.data.keys()):
                char_value, number_value, date_value = self.data[key]
                index = self.InsertStringItem(maxint, char_value)
                self.SetItemData(index, key) #muss sein
                self.SetStringItem(index, 1, str(number_value))
                self.SetStringItem(index, 2, date_value.strftime("%d.%m.%Y"))
                self.SetColumnWidth(2, wx.LIST_AUTOSIZE)
        if 1:
            # Daten in ListCtrl schreiben
            for key in list(self.data.keys()):
                
                pid, char_value, number_value, date_value = self.data[key]
                index = self.InsertStringItem(maxint, str(pid))
                self.SetItemData(index, key) #muss sein
                self.SetStringItem(index, 1, char_value)
                self.SetStringItem(index, 2, number_value)
                #self.SetStringItem(index, 2, date_value.strftime("%d.%m.%Y"))
                self.SetStringItem(index, 3, "{:,} B".format(date_value))

        self.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        self.SetColumnWidth(1, wx.LIST_AUTOSIZE)
        self.SetColumnWidth(2, wx.LIST_AUTOSIZE)
        self.SetColumnWidth(3, wx.LIST_AUTOSIZE)
                
        print('Done.')
        listmix.ColumnSorterMixin.__init__(self, numColumns = 4)
    
    
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