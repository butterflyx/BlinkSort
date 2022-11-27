import re
import json
import logging as log

import BlinkSort

class KindleSort(BlinkSort.BlinkSort):
    
    def __init__(self, filename):
        super().__init__(filename)

    def prepare_text(self):
        pass

if __name__ == "__main__":
    ks = KindleSort("../data/demo-kindle.txt")