############# BEGIN GPL 3.0 LICENSE BLOCK ##############################
#
#  This file is part of Doppelrender.
# 
#  Doppelrender is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
# 
#  Doppelrender is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with Doppelrender. If not, see <http://www.gnu.org/licenses/>.
#
############# END GPL 3.0 LICENSE BLOCK ################################

# <pep8 compliant>
# Made by Jefferson Smith and updated for Blender 2.92 by Anime Nyan

from . import dopplerender

bl_info = {
    "name": "Dopplerender",
    "description": "Smart sequence-rendering that automatically re-uses duplicate frames without re-rendering.",
    "author": "Anime Nyan, Jefferson Smith",
    "version": (1, 0, 0),
    "blender": (2, 92, 0),
    "location": "Properties > Scene > Render",
    "category": "Render",
    "warning": "",
    "support": 'COMMUNITY'
    }


def register():
    dopplerender.register()


def unregister():
    dopplerender.unregister()
