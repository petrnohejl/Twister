#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Twister version 1.0

Copyright (C)2009 Petr Nohejl, jestrab.net

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

This program comes with ABSOLUTELY NO WARRANTY!
"""

import random

def  Twister():
	side = random.randint(0,1)
	limb = random.randint(0,1)
	color = random.randint(0,3)
	
	sideArr = ["leva", "prava"]
	limbArr = ["ruka", "noha"]
	colorArr = ["cervenou", "modrou", "oranzovou", "zelenou"]
	
	print sideArr[side], limbArr[limb], "na", colorArr[color]

if (__name__=="__main__"):
	Twister()
