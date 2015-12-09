Get-WebSite | % {

$_.Name

Add-WebConfigurationProperty -filter ("system.applicationHost/sites/site[@name='{0}']/logFile/customFields" -f $_.Name)  -name "." -value @{logFieldName='X-Real-IP';sourceName='X-Real-IP';sourceType='RequestHeader'}

}
