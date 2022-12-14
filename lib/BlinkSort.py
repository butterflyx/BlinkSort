import re
import json
import logging as log

class BlinkSort:

    textlist = []

    title = ""

    chapters = {}
    
    # annotations = { "booktitle" : booktitle, "chapters" : [{ number_chapter : {"chapter_title": chapter_title , "annotations" : [annotation_1 ,... annoation_n] }] }
    annotations = {}

    def __init__(self, filename):
        try:
            with open(filename) as fp:
                self.textlist = list(filter(None, (line.rstrip() for line in fp))) # https://stackoverflow.com/questions/4842057/easiest-way-to-ignore-blank-lines-when-reading-a-file-in-python
                if len(self.textlist) == 0: # empty file
                    raise EmptyFileError
                log.debug(f"converted intext into list:\n\t-->-\n\t{self.textlist}\n\t-<--\n")
        except FileNotFoundError as e:
            log.error(f"file {filename} not found: {e}")
        
        self.prepare_text()

    def prepare_text(self) -> None:
        self.textlist.reverse() # for chronological order
        self.set_title()
        self.find_annotations()
        
    def set_title(self) -> str:
        self.title = self.annotations["booktitle"] = self.textlist[-1]
        self.textlist.pop(-1) # remove the headline so the rest of the text is all the same structure
        log.debug(f"fetched title '{self.title}' from last line. Textlist content is now:\n\t-->-\n\t{self.textlist}\n\t-<--\n")
        return self.title

    def get_title(self) -> str:
        return self.title

    def find_annotations(self) -> dict:
        log.debug(f"start function to find annotations in text")
        chapter_index = 0
        pattern = re.compile("Kapitel (\d) : (.+)")
        for line in self.textlist:
            log.debug(f"working on line:\n\t-->-\n\t{line}\n\t-<--\n")
            match = re.search(pattern, line)
            if match != None: # chapter found
                log.debug(f"chapter found")
                chapter_index = int(match.group(1))
                log.debug(f"chapter index is now {chapter_index}")
                if chapter_index not in self.chapters: # first match sets title
                    self.chapters[chapter_index] = {"chapter_title" : match.group(2)}
                    log.debug(f"chapter title is yet empty so set to '{match.group(2)}'")
            elif chapter_index > 0: # annotation found
                log.debug(f"annotation found: '{line}'")
                if "annotations" not in self.chapters[chapter_index]: # no annotions yet
                    log.debug(f"no annotions yet, so init key 'annotations' with empty list")
                    self.chapters[chapter_index]["annotations"] = []
                log.debug(f"append line to annotations")
                self.chapters[chapter_index]["annotations"].append(line)
            else:
                raise FileStructureMissmatch
        log.debug(f"done finding annotations.\n\t-->-\n\t{self.chapters}\n\t-<--\n")
        log.debug(f"merge found annotations into annotations dict with book title")
        self.annotations["chapters"] = self.chapters
        log.debug(f"final annotations dict:\n\t-->-\n\t{self.annotations}\n\t-<--\n")
        return self.annotations
    
    def get_annotations(self) -> dict:
        return self.annotations
        
    def output_markdown(self, cite=True) -> str:
        mdstr = f"# {self.annotations['booktitle']}\n"
        for index,chapter in self.annotations['chapters'].items():
            mdstr += f"\n## Kapitel {index} : {chapter['chapter_title']}\n\n"
            for annotation in chapter['annotations']:
                mdstr += f"> {annotation} \n" if cite else f"{annotation} \n"
        return mdstr

    def output_json(self,indent=4) -> str:
        return json.dumps(self.annotations, indent=indent, ensure_ascii=False)       
