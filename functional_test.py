#! /usr/bin/env python3
#encoding:utf-8

from selenium import webdriver

browser = webdriver.Firefox()
browser.get("http://localhost:8000")

assert "Django" in browser.title