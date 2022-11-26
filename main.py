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
# annotations = { "booktitle" : booktitle, "chapters" : [{ number_chapter : {"chapter_title": chapter_title , "annotations" : [annotation_1 ,... annoation_n] }] }

class BlinkSort:

    textlist = []

    title = ""

    chapters = {}

    annotations = {}

    def __init__(self, filename):
        try:
            with open(filename) as fp:
                intext = fp.read()
                log.debug(f"fetched file {filename} with content:\n{intext}")
                self.textlist = intext.strip().split("\n")
                self.textlist.reverse() # for chronological order
                log.debug(f"converted intext into list:\n{self.textlist}")
        except FileNotFoundError as e:
            log.error(f"file {filename} not found: {e} \n exiting...")
            exit()

        self.set_title()
        self.find_annotations()
        

    def set_title(self) -> str:
        self.title = self.textlist[-1]
        self.textlist.pop(-1) # remove the headline so the rest of the text is all the same structure
        log.debug(f"fetched title '{self.title}' from last line. Textlist content is now:\n{self.textlist}")
        self.annotations["booktitle"] = self.title
        return self.title

    def get_title(self) -> str:
        return self.title

    def find_annotations(self) -> dict:
        log.debug(f"start function to find annotations in text")
        chapter_index = 0
        pattern = re.compile("Kapitel (\d) : (.+)")
        for line in self.textlist:
            log.debug(f"working on line:\n{line}")
            match = re.search(pattern, line)
            if match != None: # chapter found
                log.debug(f"chapter found")
                chapter_index = int(match.group(1))
                log.debug(f"chapter index is now {chapter_index}")
                if chapter_index not in self.chapters: # first match sets title
                    self.chapters[chapter_index] = {"chapter_title" : match.group(2)}
                    log.debug(f"chapter title is yet empty so set to '{match.group(2)}'")
            elif chapter_index > 0: # annotation found
                log.debug(f"annotation found: {line}")
                if "annotations" not in self.chapters[chapter_index]: # no annotions yet
                    log.debug(f"no annotions yet, so init key 'annotations' with empty list")
                    self.chapters[chapter_index]["annotations"] = []
                log.debug(f"append line to annotations")
                self.chapters[chapter_index]["annotations"].append(line)
            else:
                raise FileStructureMissmatch
        log.debug(f"done finding annotations.\n{self.chapters}")
        log.debug(f"merge found annotations into annotations dict with book title")
        self.annotations["chapters"] = self.chapters
        return self.annotations
    
    def get_annotations(self) -> dict:
        return self.annotations
        

        


if __name__ == "__main__":
    inputfile = "./data/demo.txt"
    blink = BlinkSort(inputfile)
    print(blink.get_annotations())
