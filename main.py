from __future__ import print_function
import os
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import requests
import gdown

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly', 'https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive.readonly']
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets(
        'clientsecret.json', scope = SCOPES)
    creds = tools.run_flow(flow, store, flags) \
        if flags else tools.run(flow, store)
DRIVE = build('drive', 'v3', http=creds.authorize(Http()))


results = DRIVE.files().list(
        pageSize=30, fields="nextPageToken, files(id, name)").execute()
items = results.get('files', [])


def get_file_name():
    filename = input("Enter the file name: ")
    return filename

filename = get_file_name()
def get_id(items, filename):

    for i in items:
        if i['name'] == filename:
            fileid = i['id']
            url = "https://drive.google.com/uc?export=download&id="+i['id']
            return fileid



destination = './'
def make_url(id):
    url = "https://drive.google.com/open?id="+id
    return url


fileid = get_id(items, filename)
url = make_url(fileid)

def download_file_from_google_drive(url, id, destination):
    session = requests.Session()

    response = session.get(url, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(url, params = params, stream = True)
    print("66.66% downloaded")
    save_response_content(response, destination)


def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value
    print("33.33% downloaded")
    

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
    print("100% downloaded")
fileid = "1S-pNeJ8SZxrHDz6h3qsPbVc7k4FDR8fLOekTMp3kYSU"
if __name__ == "__main__":
    file_id = fileid
    destination = filename
    download_file_from_google_drive(url, file_id, destination)

if __name__ == "__main__":
    import sys
    if len(sys.argv) is not 3:
        print("Usage: python google_drive.py drive_file_id destination_file_path")
    else:
        # TAKE ID FROM SHAREABLE LINK
        file_id = sys.argv[1]
        # DESTINATION FILE ON YOUR DISK
        destination = sys.argv[2]
        download_file_from_google_drive(url, file_id, destination)


def clean(filename):
    with open(filename, 'r') as f2:
        data = f2.read()

    data = data.replace("<", "")
    data_list = data.split(">")

    # actual = []
    # cleaned = []
    # for i in data_list:
    #     new = i.split("\"")
    #     for j in new:
    #         if "og:description" in j:
    #             actual = new[3]
    # for i in actual.split("\n"):
    #     cleaned.append(i)
    # #os.remove(filename)
    # return cleaned[2::]
    j = 0
    # for i in data_list:
    #     if "td class=\"s0\"" in i:
    #         print(i)
    #     j+=1
    print (data_list[79])
#clean(filename)


# def append_to_csv(content, filename):
#     with open(filename, "r") as file_r:
#         file_data = file_r.read()
#     filename = filename+".csv"
#     file = open(filename, "a")
#         for i in content:
#         if i not in file_data:
#             file.write(i)
#             file.write("\n")

#append_to_csv(cleaned, filename)

# import gdown 
# import pandas as pd 
# file_id= fileid 
# url = f'https://drive.google.com/uc?id={file_id}' 
# output = open('hello.csv', "w") 

# gdown.download(url, output, quiet=False)  
# df = pd.read_csv('hello.csv') 
# print(df.head())

# from pydrive.auth import GoogleAuth

# def download_tracking_file_by_id(file_id, download_dir):
#     gauth = GoogleAuth(settings_file='../settings.yaml')
#     # Try to load saved client credentials
#     gauth.LoadCredentialsFile("../credentials.json")
#     if gauth.credentials is None:
#         # Authenticate if they're not there
#         gauth.LocalWebserverAuth()
#     elif gauth.access_token_expired:
#         # Refresh them if expired
#         gauth.Refresh()
#     else:
#         # Initialize the saved creds
#         gauth.Authorize()
#     # Save the current credentials to a file
#     gauth.SaveCredentialsFile("../credentials.json")

#     drive = GoogleDrive(gauth)

#     logger.debug("Trying to download file_id " + str(file_id))
#     file6 = drive.CreateFile({'id': file_id})
#     file6.GetContentFile(download_dir+'mapmob.zip')
#     zipfile.ZipFile(download_dir + 'test.zip').extractall(UNZIP_DIR)
#     tracking_data_location = download_dir + 'test.json'
#     return tracking_data_location

# file = download_tracking_file_by_id(fileid, './')
