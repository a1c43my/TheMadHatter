#take a command and show the help
# using param to make these cli friendly
param(
    [Parameter()]
    [String]$par,[String]$alias,[String]$pd,[String]$super
)

## make sure the log folder is present, if not create it where you are and let you know 
################
 if($par -and $pd){
        echo "adding pd to file"
        break
    }
    if($par -and $alias){
        echo "adding alias to file"
        break
    }

else{

   
    
$file = "$par.txt"

    if($par.Length -eq 5){
        echo "valid record #"
        
        $ready = Test-Path $file
    
    if($ready){
        Write-Output ""
        $folder = Test-Path "./logs/"
        if($folder){
            echo "checking for ./logs "
            Start-Sleep -Seconds 1
            echo "folder ready at $(Get-Location)\logs" 
            Start-Sleep -Seconds 1
            cls
        }
        else {
            echo "----------------------------------"
            echo "creating folder ./logs"
            Start-Sleep -Seconds 1
            New-Item -Type Directory -Name logs
            Start-Sleep -Seconds 2
            echo "folder created at $(Get-Location | Select-Object )\logs"
            Start-Sleep -Seconds 1
            cls
        }

        echo " done with record # for $par"
    }
    else {
        Write-Output "no log file for record $par yet"
        $edit = Read-Host -Prompt "Would you like to create file? [y/n]"
        if($edit -eq "y" -Or $edit -eq "yes"){
            echo "yes"
            New-Item -Type File -Path ".\logs\" -Name "$par.log"
        }
        if($edit -eq "n" -Or $edit -eq "no"){
            echo "nothing further to do for this record"
        }
    }

    }

    else {
        echo "invalid record #"
        exit
    }

    

    
}


else {
    
    Write-Output " Usage /.pse.ps1 -par [#####] -alias []"
    Write-Output " example: ./pse.ps1 -par 2222 -pd Ktran@nanoracks.gov"
}
