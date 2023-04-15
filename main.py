#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main script for BlinkSort

@author: info@butterflyx.com
"""

import sys
import argparse
import logging as log

import lib.BlinkSort as BlinkSort

def create_parser():
    output_options = ["JSON", "markdown"] # https://stackoverflow.com/questions/33786176/how-to-use-argparse-to-list-options

    parser = argparse.ArgumentParser(
        prog='main',
        description="Pretty print annotations made in Blinks from Blinkist.com and Kindle.com")

    parser.add_argument('-i','--infile', required=True, type=argparse.FileType('r'), metavar='PATH', default=sys.stdin, help='path to file with raw text')
    parser.add_argument('-o','--outfile', type=argparse.FileType('w'), metavar='PATH', default=sys.stdout, help='Output file (default: standard output)')
    parser.add_argument('-j', '--indent', type=int, help='INDENT chars for JSON output', default=4)
    parser.add_argument('-c','--cite', action='store_true', help='format markdown output as citations')
    parser.add_argument('-v', '--verbose', action='store_true', help='show debugging information')
    parser.add_argument('-f', '--output_format', action='store', required=True, choices=output_options, help="specify output format")
    
    return parser



if __name__ == "__main__":

    parser = create_parser()
    args = parser.parse_args()

    log.basicConfig(encoding='utf-8', level=log.DEBUG) if args.verbose else log.basicConfig(encoding='utf-8', level=log.ERROR)

    inputfile = args.infile
    log.debug(f"argument given as input (-f): {inputfile}")
    try:
        blink = BlinkSort.BlinkSort(inputfile.name)
    except FileNotFoundError as e:
        exit(f"File '{inputfile}' not found: {e}")

    

    if args.output_format == "markdown":
        log.debug(f"output should be formated as markdown")
        output = blink.output_markdown() if args.cite else blink.output_markdown(cite=False)            
    elif args.output_format == "JSON":
        log.debug(f"output should be formated as JSON")
        output = blink.output_json(indent=args.indent)
    else:
        raise ArgumentError

    log.debug(f"done, printing output:")
    print("-"*20)
    print(output)