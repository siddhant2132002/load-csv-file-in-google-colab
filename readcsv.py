!pip install -U -q PyDrive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials
auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)
downloaded = drive.CreateFile({'id':'1J7VtUFk-NX3amuzq9ijgxCKO4e3r7IVB'}) # replace the id with id of file you want to access
downloaded.GetContentFile('Salaries.csv') #in my case i read my Salaries.csv file which i already upload in my drive.
import pandas as pd
df=pd.read_csv('Salaries.csv')
df.info()
