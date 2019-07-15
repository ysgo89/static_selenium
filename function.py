from selenium import webdriver
from STATIC_Test import app

def main():
    app.setUp()
    app.test_static_access()