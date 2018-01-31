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
module: win_appver
version_added: "NOW"
short_description: A check the version of an installed application.
description:
  - Checks the version of an app installed on a windows host
options:
  service:
    description:
      - Display name
    required: true
    default: null
author: "Joe Sutton"
'''

EXAMPLES = '''
# Test connectivity to a windows host
ansible winserver -m win_appver  service=Adobe

# Example from an Ansible Playbook
- action: win_appver
    service: Adobe
'''

