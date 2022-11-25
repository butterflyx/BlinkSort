# /usr/bin/python3

"""
Main script for BlinkSort

@author: info@butterflyx.com
"""

import os
import re
import json
import logging as log
log.basicConfig(encoding='utf-8', level=log.DEBUG)


# "^(.+)$\n^(Kapitel (\d) :.+)$"
# 
# annotations = { booktitle, number_chapter , title_chapter , annotation }

class BlinkSort:

    text = ""

    textlist = []

    title = ""

    chapter_names = {}
    chapter_lines = []

    def __init__(self, filename):
        try:
            with open(filename) as f:
                self.text = f.read()
                log.debug(f"fetched file {filename} with content:\n{self.text}")
        except FileNotFoundError as e:
            log.error(f"file {filename} not found: {e} \n exiting...")
            exit()

        self.textlist = self.text.split('\n')
        self.set_title()

    def set_title(self) -> str:
        self.title = self.textlist[0]
        return self.title

    def get_title(self) -> str:
        return self.title

    def find_chapter_names(self) -> dict:
        log.debug(f"start function to find chapters in text")
        pattern = re.compile("Kapitel (\d) : (.+)")
        for match in pattern.finditer(self.text):
            self.chapter_names[int(match.group(1))] = match.group(2)
        return self.chapter_names

    def find_chapter_lines(self) -> list:
        for index, line in enumerate(self.textlist):
            if re.fullmatch(r"Kapitel (\d) : .+", line):
                log.debug(f"found match for chapter in line {index}")
                self.chapter_lines.append(index)
        return self.chapter_lines

    def find_annotations(self):
        log.debug(f"start function to find annotations in text")
        if (len(self.chapter_lines) == 0):
            self.find_chapter_lines()
        index_list = self.chapter_lines
        index_list.insert(0, 0)
        index = -1
        while index > -(len(index_list)):
            number_of_annotations = (index_list[index]-index_list[index-1])-1
            log.debug(f"found {number_of_annotations} annotations between line {index_list[index]} and line {index_list[index-1]}")
            for line in range(number_of_annotations):
                log.debug(f"annoation: {self.textlist[index_list[index-1]+1]}")
            index -= 1
        

        


if __name__ == "__main__":
    inputfile = "./data/demo.txt"
    blink = BlinkSort(inputfile)
    blink.find_chapter_names()
    print(blink.find_chapter_lines())
    blink.find_annotations()