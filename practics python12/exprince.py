import clamav
scanner = clamav.Scanner()
scanner.loadDB()
scanner.scanFile('clam.exe')
(1, 'Clamav.Test.File-6')