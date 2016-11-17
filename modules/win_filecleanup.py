#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2012, Michael DeHaan <michael.dehaan@gmail.com>, and others
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

# this is a windows documentation stub.  actual code lives in the .ps1
# file of the same name

DOCUMENTATION = '''
---
module: win_filecleanup
version_added: "NOW"
short_description: cleans up files X days old.
description:
  - Checks the existence of a certificate on a windows host
options:
  days:
    description:
      - Number of days a file can exist 
    required: true
    default: 45
  path:
    description:
      - Path to be cleaned
    required: false
    default: C:\installs\
author: "Joe Sutton"
'''

EXAMPLES = '''
# Test connectivity to a windows host
ansible winserver -m win_filecleanup  days=30 path=C:\installs\

# Example from an Ansible Playbook
- action: win_filecleanup
    days: 30
    path: "C:\installs\"
'''

