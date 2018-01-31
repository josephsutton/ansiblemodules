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
module: win_cert
version_added: "NOW"
short_description: A check the existence of a certificate.
description:
  - Checks the existence of a certificate on a windows host
options:
  thumb:
    description:
      - Thumbprint for certificate
    required: true
    default: 81233544102891a702a430b4eeeb4b8f07f2e10
author: "Joe Sutton"
'''

EXAMPLES = '''
# Test connectivity to a windows host
ansible winserver -m win_cert  thumb=81234567890abcdef0987654321abcdef12345678

# Example from an Ansible Playbook
- action: win_cert
    thumb: 1234567890abcdef0987654321abcdef12345678
	
- action: win_cert thumb=1234567890987654321123456789098765432112
'''

