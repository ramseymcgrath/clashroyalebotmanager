import config
import process
import os, os.path
import subprocess

###
# Globals
###
CONFIG = config.configuration()

###
# BotCode
###

#TODO: Figure how to handle CRBot from the CLI

def getBotList(xmlPath):
    botsToRun = process.process(xmlPath)

def spinUpBot(bot,memuPath):
    subprocess.call(["MMmuConsole", bot.name])

def main():
    bots = getBotList(CONFIG.BotConfigXML)
    for bot in bots:
        spinUpBot(bot, CONFIG.MEMuPath)
    print(MEmu processes started)