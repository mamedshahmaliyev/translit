#!/bin/sh

echo 'python -m venv venv \n venv\Scripts\pip install -r requirements'
venv/bin/python translit.py
