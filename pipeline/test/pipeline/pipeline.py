#test.pipeline.bat
import os, sys, csv, time, logging
import datetime as dt
from  datetime import datetime
import decimal
from os.path import split, join, isdir, basename, isfile
from pprint import pprint as pp
from cli_layer.utils import timer, get_err
from pathlib import Path
from cli_layer.common import *
from cli_layer.fmt import  pfmt, pfmtv, pfmtd, psql
from pipeline.test.pipeline.include.utils import usage
#import cli_layer.pipeline.test.utils as ppl_utils
from cli_layer.pipeline.utils import get_params

e=sys.exit

log = logging.getLogger()


import cli_layer.config.app_config as app_config
apc = app_config.apc

@timer (basename(__file__))
def test_pipeline(**kwargs):
	"""	 
	Location	 : test\pipeline	
	Params : 
		        "param1" - param 0
        "param2" - param 1
	Num of params: 2
	Usage: python cli.py -nop 1 -r DEV -p test\pipeline -pa param1 param2
	"""
	cp, params=usage(**kwargs)
	limit	= kwargs['lame_duck']
	param1,param2 = params
	#TODO
	

if __name__=="__main__":
	kwargs={} #TODO
	test_pipeline(**kwargs)

	