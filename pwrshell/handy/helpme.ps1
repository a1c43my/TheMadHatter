#take a command and show the help
# using param to make these cli friendly
param(
    [Parameter()]
    [String]$cmd
)
if($cmd){
    cls
  Get-help $cmd -examples
echo "help for $cmd"  
}
else {Write-Output " Usage /.helpme.ps1 -cmd []"}
