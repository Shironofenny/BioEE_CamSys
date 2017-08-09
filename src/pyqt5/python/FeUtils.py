#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

def feFindDir(dirname, hier):
  ''' Find the directory specified by the $dirname in upto $hier levels
  '''

  # General sanity checks
  if not dirname:
    return None

  source_path = dirname

  for i in range(hier+1):
    if (os.path.isdir(source_path)):
      return source_path
    else :
      source_path = '../' + source_path

  # If can't find the directory in defined number of hierachies, then return None
  return None

def isNumber(text):
  try :
    value = float(text)
  except ValueError :
    return False
  else :
    return value
