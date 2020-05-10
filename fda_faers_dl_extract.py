import zipfile
import urllib.request
import glob, os, shutil

## Define Year and Quarter ranges
years = list(range(2013, 2018))
quarters = list(range(1, 5))
# pre 2012 q4 should be "aers" not "faers"
base_url = "https://fis.fda.gov/content/Exports/faers_ascii_"
test_add = base_url + str(years[0]) + "q" + str(quarters[0]) + ".zip"

download_urls = []

## Generate list of URLS for download
for i in range(0, len(years)):
    for j in range(0, len(quarters)):
        temp = base_url + str(years[i]) + "q" + str(quarters[j]) + ".zip"
        download_urls.append(temp)

##
base_path = "E:/SQL/FDA_FAERS/Python_DL/fda_faers_dl_extract/TEST/"
split_val = "https://fis.fda.gov/content/Exports/"

## Download each file, extract to txt files to DATA FOLDER, delete temporary files
for k in range(0, len(download_urls)):
    end_path = download_urls[k].split(split_val, 1)[1]
    filename = base_path + end_path
    urllib.request.urlretrieve(download_urls[k], filename)
    os.makedirs("E:/SQL/FDA_FAERS/Python_DL/fda_faers_dl_extract/TEST/TEMP")
    with zipfile.ZipFile(filename) as zip:
        zip.extractall("E:/SQL/FDA_FAERS/Python_DL/fda_faers_dl_extract/TEST/TEMP")
        files = glob.iglob(os.path.join("E:/SQL/FDA_FAERS/Python_DL/fda_faers_dl_extract/TEST/TEMP/ascii", "*.txt"))
        for file in files:
            if os.path.isfile(file):
                shutil.copy2(file, "E:/SQL/FDA_FAERS/Python_DL/fda_faers_dl_extract/TEST/DATA")
    shutil.rmtree("E:/SQL/FDA_FAERS/Python_DL/fda_faers_dl_extract/TEST/TEMP/")

## Repeat above process for aers data

years = list(range(2004, 2013))
quarters = list(range(1, 5))
# pre 2012 q4 should ve "aers" not "faers"
base_url = "https://fis.fda.gov/content/Exports/aers_ascii_"
test_add = base_url + str(years[0]) + "q" + str(quarters[0]) + ".zip"
# print(test_add)

download_urls = []

for i in range(0, len(years)):
    for j in range(0, len(quarters)):
        temp = base_url + str(years[i]) + "q" + str(quarters[j]) + ".zip"
        download_urls.append(temp)

# print(download_urls)


base_path = "E:/SQL/FDA_FAERS/Python_DL/fda_faers_dl_extract/TEST/"
split_val = "https://fis.fda.gov/content/Exports/"

for k in range(0, len(download_urls)):
    end_path = download_urls[k].split(split_val, 1)[1]
    filename = base_path + end_path
    urllib.request.urlretrieve(download_urls[k], filename)
    os.makedirs("E:/SQL/FDA_FAERS/Python_DL/fda_faers_dl_extract/TEST/TEMP")
    with zipfile.ZipFile(filename) as zip:
        zip.extractall("E:/SQL/FDA_FAERS/Python_DL/fda_faers_dl_extract/TEST/TEMP")
        files = glob.iglob(os.path.join("E:/SQL/FDA_FAERS/Python_DL/fda_faers_dl_extract/TEST/TEMP/ascii", "*.txt"))
        for file in files:
            if os.path.isfile(file):
                shutil.copy2(file, "E:/SQL/FDA_FAERS/Python_DL/fda_faers_dl_extract/TEST/DATA")
    shutil.rmtree("E:/SQL/FDA_FAERS/Python_DL/fda_faers_dl_extract/TEST/TEMP/")
