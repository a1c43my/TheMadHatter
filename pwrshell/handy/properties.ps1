#take input and show properties of object

param(
    [Parameter()]
    [String]$obj
)
if($obj){
    cls
  Get-Memmber -InputObject $obj
  #Select-object -InputObject $obj -Property *
echo "help for $obj"  
}
else {Write-Output " Usage /.helpme.ps1 -obj []"}
