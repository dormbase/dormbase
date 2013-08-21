# Dormbase -- open-source dormitory database system
# Copyright (C) 2012 Alex Chernyakhovsky <achernya@mit.edu>
#                    Drew Dennison       <dennison@mit.edu>
#                    Isaac Evans         <ine@mit.edu>
#                    Luke O'Malley       <omalley1@mit.edu>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.conf import settings
from django.shortcuts import redirect
        
def report(request):
    # Base URL
    url = 'https://insidemit-apps.mit.edu/apps/building_services/CreateResidRepairOrder.action?sapSystemId=PS1'
    
    # Auto-Fill Building Number
    if hasattr(settings, 'BUILDING'):
        url += '&pageInfo.bldg1=' + settings.BUILDING + '&pageInfo.contactInfo.bldg=' + settings.BUILDING
    
    # TODO: fill in user's room, phone number, check if they actually live here
    
    return redirect(url)
