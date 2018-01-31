# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.


# WANT_JSON
# POWERSHELL_COMMON

$params = Parse-Args $args $false;
$service = Get-AnsibleParam -obj $params -name "service" -type "str" -failifempty $true



$software= Get-ItemProperty -path HKLM:\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\* | Where-Object {$_.DisplayName -contains ($service)};

if ($software.DisplayName -contains $service)
{ $outcome = $software.DisplayVersion
}
else
{ $outcome = "fail"
}
#write-host $outcome
$result = New-Object psobject @{
    changed = $false
    win_appver = $outcome
};

Exit-Json $result;
