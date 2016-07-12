#!/usr/bin/python
# -*- coding: utf-8 -*-

import collections
import json
import os
import re

def main():
    # Open output file
    with open('README.md', 'w') as f:
        
        # Header file
        header =    '# TODAY I LEARNED\n'
        header +=   '\n'
        header +=   '* Idea stolen from: https://github.com/jbranchaud/til'
        header +=   '\n'
        header +=   '\n'
        
        f.write(header)
    
        # For each directory/section

        l =  os.walk(os.getcwd())
        sections = [x[0] for x in l]
        for section in sections:
            title = section.replace(os.getcwd(),'').replace('/','')
            if len(title) > 0 and title[0] != '.':
                # Write title
                f.write("# " + title + "\n\n")

                # Get all available files in the directory
                t = os.listdir(section)
                # For each file
                for til in t:
                    if len(til) > 0 and til[0] != '.':
                        f.write('[ ' + til.replace('-',' ') + ' ] (' + title + '/' + til + ')\n')
        
            f.write('\n')
            
if __name__ == '__main__':
    main()
