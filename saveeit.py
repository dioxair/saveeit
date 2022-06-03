import os
import requests

def main():
    print("Please enter the URL of the Reddit video you want to download.")

    redditURL = input(">> ")[:-1]+".json"
