#!  /global/freeware/Linux/RHEL6/python-3.7.0/bin/python
#/global/freeware/Linux/RHEL6/python-2.7.15/bin/python
"""
__File__          = "main.py"
__Description__   = ""
__Author__        = "MrChuckomo"
__Version__       = "v1.0.0"
__Creation_Date__ = "15-Jun-2017"
"""

from view import board as BoardGui
from model import kanban_db as Db

Db.InitDb()

BoardGui.drawWindow()
