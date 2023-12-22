# BlinkSort

Pretty print annotations made in Blinks from Blinkist.com and Kindle.com

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
3. click and drag over the annotations **per book**, beginning with the title of the book
4. copy to clipboard `Strg+C`
5. paste the content to an empty file and safe it relative to the script as *.txt file
6. run script

### Script parameters
```
python3 main.py -h
usage: main [-h] -i PATH [-o PATH] [-j INDENT] [-c] [-v] -f {JSON,markdown}

Pretty print annotations made in Blinks from Blinkist.com and Kindle.com

optional arguments:
  -h, --help            show this help message and exit
  -i PATH, --infile PATH
                        path to file with raw text
  -o PATH, --outfile PATH
                        Output file (default: standard output)
  -j INDENT, --indent INDENT
                        INDENT chars for JSON output
  -c, --cite            format markdown output as citations
  -v, --verbose         show debugging information
  -f {JSON,markdown}, --output_format {JSON,markdown}
                        specify output format

```
### Working on multiple files

There is no batch option (yet), so the easiest way is to safe a txt for each book in a separate directory and then run this line of bash script:
`for f in $(find . -iname '*.txt'); do python3 /home/Path-to-BlinkSort/main.py -i $f -f markdown -o ./$f.md; rm -f $f; done`
which will output a .md file and remove the original .txt file.



## roadmap

- [x] option to output as JSON
- [x] option to output as Markdown
- [ ] works for multiple blinks at once
- [ ] multi languages
- [ ] use webscraper
- [ ] works as well for [Kindle highlights](https://kindle.amazon.com/your_highlights)
- [x] opt. write output to file

