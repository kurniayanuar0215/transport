import paramiko
import datetime
import os

now = datetime.datetime.now()
week = str(datetime.datetime.utcnow().isocalendar()[1]-1)
year = str(now.year)

ip = '10.54.18.23'
username = 'transport'
password = 'Transport2017#'

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip, username=username, password=password)
sftp = ssh.open_sftp()

checkpath = '''/home/transport/output/RAW_DATA/04-JAWABARAT/'''+year+'''/WEEK'''+week
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('cd ' + checkpath + ' && ls | wc -l')

x = int(ssh_stdout.read().decode("utf-8"))

if x == 4:

    localpath = '''F:/KY/transport/download/RAWDATA_3G_'''+year+'''_W'''+week+'''_R04JAWABARAT.xlsb'''
    remotepath = '''/home/transport/output/RAW_DATA/04-JAWABARAT/'''+year+'''/WEEK'''+week+'''/RAWDATA_3G_'''+year+'''_W'''+week+'''_R04JAWABARAT.xlsb'''
    sftp.get(remotepath,localpath)

    localpath = '''F:/KY/transport/download/RAWDATA_4G_'''+year+'''_W'''+week+'''_R04JAWABARAT.xlsb'''
    remotepath = '''/home/transport/output/RAW_DATA/04-JAWABARAT/'''+year+'''/WEEK'''+week+'''/RAWDATA_4G_'''+year+'''_W'''+week+'''_R04JAWA BARAT.xlsb'''
    sftp.get(remotepath,localpath)

    os.environ["https_proxy"] = "https://10.59.66.1:8080"
    os.system("telegram-send Transport_W"+week+"_Updated")

    os.system('python' + ' ' + 'F:/KY/transport/bundlefile.py')

else:
    os.environ["https_proxy"] = "https://10.59.66.1:8080"
    os.system("telegram-send Transport_W"+week+"_Not_Updated")

sftp.close()
ssh.close()

