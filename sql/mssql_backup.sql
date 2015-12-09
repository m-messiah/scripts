DECLARE @basename varchar(50)
DECLARE @backupname varchar(150)
DECLARE @logname varchar(150)

SET @basename='WebSitesRemoteLog'
SET @backupname=N'\\web-sites-5\F\' + @basename + '.bak'
SET @logname=N'\\web-sites-5\F\' + @basename + '_log.bak'



BACKUP DATABASE @basename TO DISK = @backupname;
BACKUP LOG @basename TO DISK = @logname;
GO
