import os
from datetime import date

# DATE
today = date.today()
dateFormat = today.strftime("%b-%d-%Y")
indexMonth = int(today.strftime("%m")) 
ESmonth = {1:'Enero',2:'Febrero',3:'Marzo',4:'Abril',5:'Mayo',6:'Junio',7:'Julio',8:'Agosto',9:'Septiembre',10:'Octubre',11:'Noviembre',12:'Diciembre'}
year = today.strftime("%Y")

# DIRECTORIES
nameDirMain = 'DOCUMENTOS_DESCARGAS'
nameSubDir  = year+'_'+ESmonth[indexMonth]

# QUERY DIRS
home_folder     = os.getenv('USERPROFILE')
query_home      = home_folder+"\Documents"
queryMainDir    = home_folder+"\Documents\\"+nameDirMain 
querySubDir     = queryMainDir+'\\'+nameSubDir
queryDownload   = home_folder+"\Downloads"

# --------------------------------------------------------------------

# Verify if exist the main directory
def mainDir():
    #print(queryMainDir)
    if(not os.path.exists(queryMainDir)):
        os.system("cd "+query_home+" && mkdir "+nameDirMain)          
        subDirVerify()       
    else:         
        subDirVerify()

# Verify if exist the Sub-directory
def subDirVerify():
    if(not os.path.exists(queryMainDir+'\\'+nameSubDir )):
        os.system("cd "+queryMainDir+" && mkdir "+nameSubDir)  

# This function is to move all files (.pdf, .xlsx, .docx) into the sub directory from Downloads directory
def insertFilesIntoSubDir():    
    for f in os.listdir(queryDownload):
        if f.endswith('.pdf') or f.endswith('.xlsx') or f.endswith('.docx') or f.endswith('.txt') or f.endswith('.csv'): 
            archivo = f.replace(' ', '_')   
            os.rename(queryDownload+'\\'+f,queryDownload+'\\'+archivo)
            print(archivo)
            os.system("move "+queryDownload+"\\"+archivo+" "+querySubDir+"\\") 

# Execute script
mainDir()
insertFilesIntoSubDir()
