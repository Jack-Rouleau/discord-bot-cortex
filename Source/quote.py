import asyncio

from helpers.file_helper import FileHelper

fileName = "quote_file.json"

class Quote():
    def add(message):
        if not FileHelper.exists(fileName):
            FileHelper.create(fileName)
        FileHelper.add_line(fileName, message)

    def random():
        quote = "Oopsy Daisy! Nothing to show here. Start by adding a first quote `!addquote [quote]`."
        if FileHelper.exists(fileName):
            quote = FileHelper.read_random(fileName)
        return quote