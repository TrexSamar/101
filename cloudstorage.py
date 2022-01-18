import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token             
    
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token) 
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BAWn5R8zNONhqLjYS3Nj9ypU4w5PPGkXj16zkIjOPxOVR1AtKiR5AYObb-xl9zGLTm2bs6SXXGkUdN4bOKYTM1DW6yFGNLagBqO2NZg0L81yceEPsn_KbNQvfiMAS8OGteyMC70'        
    transferData = TransferData(access_token)
    file_from = input('Enter the file path to tranfer: ')
    file_to = input('Enter the full path to upload to dropbox: ')
    transferData.upload_file(file_from, file_to)
    print('File has been moved')
    
main()