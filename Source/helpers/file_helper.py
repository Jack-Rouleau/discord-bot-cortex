import os
import random

class FileHelper():

    def exists(file_name):
        return os.path.isfile(file_name)

    def add_line(file_name, line):
        with open(file_name, "a") as file:
            file.write(line)
            file.write('\n')

    def create(file_name):
        open(file_name, 'a').close()

    def read_random(file_name):
        return random.choice(open(file_name).readlines())