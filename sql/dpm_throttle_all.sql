DECLARE @w int SET @w = (SELECT [WorkHoursTransmissionRate] from tbl_AM_InstalledAgent WHERE InstallID = 'F308BBDC-DE95-4502-A721-A8BB95D79132') 
DECLARE @n int SET @n = (SELECT [NonWorkHoursTransmissionRate] from tbl_AM_InstalledAgent WHERE InstallID = 'F308BBDC-DE95-4502-A721-A8BB95D79132') 
DECLARE @t nvarchar(max) SET @t = (SELECT [ThrottlingSettings] from tbl_AM_InstalledAgent WHERE InstallID = 'F308BBDC-DE95-4502-A721-A8BB95D79132')

UPDATE [dbo].[tbl_AM_InstalledAgent]
   SET [IsThrottled] = 1
      ,[WorkHoursTransmissionRate] = @w
      ,[NonWorkHoursTransmissionRate] = @n
      ,[ThrottlingSettings] = @t

GO

