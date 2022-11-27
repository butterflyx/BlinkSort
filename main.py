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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='main')
    parser.add_argument('-f','--infile', required=True, type=argparse.FileType('r'), default=sys.stdin, help='path to file with raw text')
    parser.add_argument('-i', '--indent', type=int, help='INDENT chars for JSON output', default=4)
    parser.add_argument('-c','--cite', action='store_true', help='format markdown output as citations')
    parser.add_argument('-v', '--verbose', action='store_true', help='show debugging information')
    parser.add_argument('-o', '--output_format', action='store', required=True, help="specify output format: J = JSON or M = Markdown")
    args = parser.parse_args()

    log.basicConfig(encoding='utf-8', level=log.DEBUG) if args.verbose else log.basicConfig(encoding='utf-8', level=log.ERROR)

    inputfile = args.infile
    log.debug(f"argument given as input (-f): {inputfile}")
    try:
        blink = BlinkSort.BlinkSort(inputfile.name)
    except FileNotFoundError as e:
        exit(f"File '{inputfile}' not found: {e}")

    if args.output_format == "M":
        log.debug(f"output should be formated as markdown")
        output = blink.output_markdown() if args.cite else blink.output_markdown(cite=False)            
    elif args.output_format == "J":
        log.debug(f"output should be formated as JSON")
        output = blink.output_json(indent=args.indent)
    else:
        raise ArgumentError

    log.debug(f"done, printing output:")
    print("-"*20)
    print(output)