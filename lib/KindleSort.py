import re
import json
import logging as log

import BlinkSort

class KindleSort(BlinkSort.BlinkSort):

    author = ""
    last_access = ""
    
    def __init__(self, filename):
        super().__init__(filename)

    def prepare_text(self) -> None:
        self.set_title()

    def set_title(self) -> str:
        self.title = self.annotations["booktitle"] = self.textlist[0]
        self.textlist.pop(0) # remove the headline so the rest of the text is all the same structure
        self.author = self.textlist[0]
        self.textlist.pop(0)
        self.last_access = self.textlist[0]
        self.textlist.pop(0)
        self.textlist.pop(0) # dicard number of highlight and notes
        log.debug(f"fetched title '{self.title}', author '{self.author}' and last access date '{self.last_access}'.")
        log.debug(f"Textlist content is now:\n\t-->-\n\t{self.textlist}\n\t-<--\n")
        return self.title

if __name__ == "__main__":
    log.basicConfig(encoding='utf-8', level=log.DEBUG)
    ks = KindleSort("../data/demo-kindle.txt")