DECLARE @basename varchar(50)
DECLARE @backupname varchar(150)
DECLARE @logname varchar(150)
DECLARE @outname varchar(150)
DECLARE @outlog varchar(150)
SET @basename='WebSitesRemoteLog'
SET @backupname='F:\' + @basename + '.bak'
SET @logname='F:\' + @basename + '_log.bak'
SET @outname='F:\MSSQL\' + @basename + '.mdf'
SET @outlog='F:\MSSQL\' + @basename + '_1.ldf'



RESTORE DATABASE @basename
FROM DISK = @backupname
WITH REPLACE, NORECOVERY,
MOVE 'WebSitesRemoteLog' TO @outname,
MOVE 'WebSitesRemoteLog_log' TO @outlog


RESTORE LOG @basename
FROM DISK = @logname
WITH NORECOVERY;
GO
