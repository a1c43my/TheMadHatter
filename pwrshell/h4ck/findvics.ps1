#take a command and show the help
# using param to make these cli friendly
param(
    [Parameter()]
    [String]$scan,
    [String]$type
)

if($type = '24'){
    if($scan){
    #PING.EXE -n 2 $scan
Write-Output "scanned $scan.1/24" ; exit }
}
if($scan){
    #PING.EXE -n 2 $scan
Write-Output "pinged host $scan";
}
else {
    Write-Output " Usage /.findvics.ps1 "
    Write-Output "-scan x.x.x";
    Write-Output "-type [8/16/24/32]"
    Write-Output "Example: ./findvics.ps1 -scan 10.0.0 -type 24 ( scans 10.0.0.1/24"
    Write-Output "Example: ./findvics.ps1 -scan 10.0.0 -type 16 ( scans 10.0.0.1/16"
}
