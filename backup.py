import shutil
import os
import datetime

def create_backup(source_path,destination_path):
    date_name=datetime.date.today()
    backup_name=os.path.join(destination_path,f"backup_{date_name}")
    try:
        shutil.make_archive(backup_name,'gztar',source_path)
        print("Backup Completed")
    except Exception as e:
        print(e)    

source_path=input("enter the following he source _path")#r"/Users\Dell\Downloads\python"
destination_path= input("enter the folloeing the destinetion_path")  #r"/Users\Dell\Downloads\python\backups" 


#here is the calling the following the function source path and the folloeing the destination path

create_backup(source_path,destination_path)