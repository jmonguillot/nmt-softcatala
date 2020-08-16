#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2020 Jordi Mas i Hernandez <jmas@softcatala.org>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

import re
import sys

def main():

    if len(sys.argv) < 2:
        print("Use: pattern to search")
        return

    find_str = f'.*{sys.argv[1]}.*'
    with open('src-train.txt') as fp_src, open('tgt-train.txt') as fp_tgt:
        line_src = fp_src.readline()
        line_tgt = fp_tgt.readline()

        while line_src and line_tgt:
           line_src = fp_src.readline()
           line_tgt = fp_tgt.readline()

           if re.match(find_str, line_src, re.M|re.I):

               if not re.match('.*t-shirt.*', line_src, re.M|re.I): 
                    print(line_src)
                    print(line_tgt)
                    print("---")

    
if __name__ == "__main__":
    main()
