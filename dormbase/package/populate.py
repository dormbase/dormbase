# Dormbase -- open-source dormitory database system
# Copyright (C) 2012 Alex Chernyakhovsky <achernya@mit.edu>
#                    Drew Dennison       <dennison@mit.edu>
#                    Isaac Evans         <ine@mit.edu>
#                    Luke O'Malley       <omalley1@mit.edu>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

""" This file populates test packages """

from dormbase.core.models import Resident
from dormbase.package.models import Package
import random

def import_test_packages():
    residents = Resident.objects.all()[0:random.randint(5, 15)]

    comments = ["", "Perishable, pick up as soon as possible", "This is a comment.", "Hello, world"]

    for r in residents:
        if random.randint(0,5) == 5:
            o = True
        else:
            o = False
        
        l = random.choice(['A', 'B', 'C', 'D', 'Floor'])
        c = random.choice(comments)
    
        p = Package(recipient = r,
                    urgent = o,
                    comment = c,
                    location = l)
        p.save()

    print 'Packages COMPLETE'
