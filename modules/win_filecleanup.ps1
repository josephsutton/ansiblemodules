#!powershell
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


# WANT_JSON
# POWERSHELL_COMMON

$params = Parse-Args $args $false;
$days = Get-AnsibleParam -obj $params -name "days" -type "str" -failifempty $false
$path = Get-AnsibleParam -obj $params -name "path" -type "str" -failifempty $false

#[CmdletBinding()]
#    param(
#        [Parameter(Position=0,mandatory=$true)]
#        [int]$days=$(throw "Delete files that are more than how mand days?"),
#        [Parameter(Position=0,mandatory=$true)]
#        [string]$path=$(throw "Where are the files you want to delete")
#    )

#    Write-Host "deleting files that are more than $days from $path"

    $limit = (Get-Date).AddDays(-$days)
    
    # Delete files older than the $limit.
    Get-ChildItem -Path $path -Recurse -Force | Where-Object { !$_.PSIsContainer -and $_.CreationTime -lt $limit } | Remove-Item -Force

    # Delete any empty directories left behind after deleting the old files.
    Get-ChildItem -Path $path -Recurse -Force | Where-Object { $_.PSIsContainer -and (Get-ChildItem -Path $_.FullName -Recurse -Force | Where-Object { !$_.PSIsContainer }) -eq $null } | Remove-Item -Force -Recurse

Exit-Json $result;
