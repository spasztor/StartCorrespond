"""Builds the project using py2exe with various, specified configurations"""
from distutils.core import setup
import py2exe

setup(windows=[{"script" : "../StartDatabase2013.pyw",
                "icon_resources" : [(1, "../_msc/icon.ico")]}],
      zipfile=None,
      options={"py2exe" : {"bundle_files" : 1,
                           "compressed" : 1,
                           "dist_dir" : "../release/_latest/bin"}})
