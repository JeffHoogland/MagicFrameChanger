#!/bin/bash
rm ui_*.py
rm ui_*.pyc
pyside-uic selector.ui > ui_selector.py
