# BlinkSort

Sort annotations made in Blinks from Blinkist.com

## Background
Blinkist is a service which provides blinks for books. Texts can be highlighted in the app and accessed via https://www.blinkist.com/de/nc/highlights 
Unfortuantely the available sortings are either chronological or by book, with the oldest first. 

This script helps to locally archive the annotations by book and in chronological order.

## Features
- create either markdown or JSON output
- remove duplicate headlines
- reorder the elements chronologically

## How to use:
1. go to https://www.blinkist.com/de/nc/highlights 
2. choose "Hinzugefügt am" for sorting
3. click and drag over the annotations per book, beginning with the title of the book
4. copy to clipboard `Strg+C`
5. paste the content to an empty file and safe it relative to the script as *.txt file
6. run script

### Script parameters
```
usage: main [-h] -f INFILE [-i INDENT] [-c] [-v] -o OUTPUT_FORMAT

optional arguments:
  -h, --help            show this help message and exit
  -f INFILE, --infile INFILE
                        path to file with raw text
  -i INDENT, --indent INDENT
                        INDENT chars for JSON output
  -c, --cite            format markdown output as citations
  -v, --verbose         show debugging information
  -o OUTPUT_FORMAT, --output_format OUTPUT_FORMAT
                        specify output format: J = JSON or M = Markdown
```

## roadmap

- [x] option to output as JSON
- [x] option to output as Markdown
- [ ] multi languages
- [ ] use webscraper

