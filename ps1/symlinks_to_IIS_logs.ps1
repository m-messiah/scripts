$computers = "example1", "example2", "example3"
ForEach ($computer in $computers) {
    $sites = [adsi]"IIS://$computer/W3SVC"
    $children = $sites.children 
    ForEach ($child in $children) { 
        If ($child.KeyType -eq "IIsWebServer") { 
            $name = $child.AppPoolId.ToString()
            $id = $child.Name.ToString()
            $directory = "\\$computer\c`$\inetpub\logs\LogFiles\W3SVC$id"
            New-Item -ItemType directory -ErrorAction Ignore -Path $name\IIS
            Invoke-Expression "cmd /c mklink /D $name\IIS\$computer $directory"
        }                                                             
    }
}
