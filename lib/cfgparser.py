#/usr/bin/env python3
"""configuration funcs to get parameters from user"""
import os
import configparser
from utils import utils

print_prefix='lib.cfgparser>>'

def read_cfg(config_file):
    """ Simply read the config files """
    config=configparser.ConfigParser()
    config.read(config_file)
    return config

def write_cfg(cfg_hdl, config_fn):
    """ Simply write the config files """
    with open(config_fn, 'w') as configfile:
        cfg_hdl.write(configfile)

def get_varlist(cfg_itm):
    varlist=cfg_itm.split(',')
    varlist=[ele.strip() for ele in varlist]
    return varlist
