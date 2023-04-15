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
    parser.add_argument('-o','--outfile', type=argparse.FileType('w'), metavar='PATH', default=sys.stdout, help='Output file (default: standard output)') # do not set dest='output' or it wont work
    parser.add_argument('-j', '--indent', type=int, help='INDENT chars for JSON output', default=4)
    parser.add_argument('-c','--cite', action='store_true', help='format markdown output as citations')
    parser.add_argument('-v', '--verbose', action='store_true', help='show debugging information')
    parser.add_argument('-f', '--output_format', action='store', required=True, choices=output_options, help="specify output format")
    
    args = parser.parse_args()

    return args



if __name__ == "__main__":

    args = create_parser()
    
    log.basicConfig(encoding='utf-8', level=log.DEBUG) if args.verbose else log.basicConfig(encoding='utf-8', level=log.ERROR)

    inputfile = args.infile
    log.debug(f"argument given as input (-i): {inputfile}")
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

    log.debug(f"done, processing output")

    if outfile := args.outfile:
        log.debug(f"argument given as output file (-o): {outfile}")
        log.debug(f"writing output to outfile")
        outfile.write(output)
    else:
        log.debug(f"printing output to stdout")
        print("-"*20)
        print(output)