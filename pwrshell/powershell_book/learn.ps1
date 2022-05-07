<# 
 working with some powershell concepts to try and make something useful

 paramas and the try statements i need

 for now the params are simply a file name and what you would like to do



#>
#first function
 

param(
    [Parameter()]
    [String]$vic,[String]$port,[String]$file,[String]$super,[String]$site,[String]$count,[String]$m
)
function filecheck($file) {
    Test-Path $file
}

function hostping($sitein,$c){
    ping $sitein
}


function sitescan($sitein){
    wget "http://$sitein"
}


if($m -eq "site" -and $count){
    echo "sending ping to $vic"
    sitescan($vic)
    break
}
if($m -eq "site" -and !($count)){
    echo "pinging nobody, you forgot the count"
    filecheck("./test.txt")
    break
}
if($m -eq "vic" -and $count){
    echo "sending ping to $vic"
    hostping($vic,$count=$count)
    break
}
else {Write-Output " Usage /.learn.ps1 -m [site/vic] to see help []"}
