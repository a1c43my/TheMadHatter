#take a command and show the help
# using param to make these cli friendly
param(
    [Parameter()]
    [String]$par,[String]$alias,[String]$pd
)

## make sure the log folder is present, if not create it where you are and let you know 
$folder = Test-Path "./logs/"
if($folder){

    echo "folder ready at $(Get-Location)\logs"
}
else {
    New-Item -Type Directory -Name logs
    echo "folder created at $(Get-Location)\logs"
}
################


if($par){
    
 $ready = Test-Path "$par.txt"
 
 if($ready){
      Write-Output "it exists"
 }
 else {
      Write-Output "not yet"
 }


echo "record # for $par"  
}
else {
    
    Write-Output " Usage /.pse.ps1 -par [#####] -alias []"
    Write-Output " example: ./pse.ps1 -par 2222 -pd Ktran@nanoracks.gov"
}
