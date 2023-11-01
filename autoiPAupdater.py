import os
import zipfile
import time
import sys
import plistlib
import shutil
import subprocess

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_folders_if_not_exist(path):
    folders_to_create = ["decrypted_iPA", "modded_iPA", "tweaks"]
    for folder in folders_to_create:
        folder_path = os.path.join(path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def unzip_ipa(ipa_path):
    clear_terminal()
    file_name_no_ipa = os.path.basename(ipa_path)[:-4]
    zip_path = ipa_path.replace(".ipa", ".zip")

    if os.path.exists(ipa_path):
        os.rename(ipa_path, zip_path)
        print("iPA file successfully renamed to .Zip")
        time.sleep(1)
        clear_terminal()
    else:
        print("The .iPA file could not be found. Try again...")
        sys.exit()

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(os.path.dirname(zip_path))

    payload_path = os.path.join(os.path.dirname(zip_path), "Payload")

    app_folder = None
    for item in os.listdir(payload_path):
        if item.endswith(".app"):
            app_folder = item
            break

    if app_folder is None:
        print("App folder not found. Try it again...")
        sys.exit()

    app_path = os.path.join(payload_path, app_folder)
    return app_path, file_name_no_ipa, zip_path, payload_path

path = "/Users/jonasb./Desktop/autoupdater"
create_folders_if_not_exist(path)

ipa_path = input("Please enter the path to the IPA file:\n")
clear_terminal()
app_path, file_name_no_ipa, zip_path, payload_path = unzip_ipa(ipa_path)

info_plist_path = os.path.join(app_path, "Info.plist")
with open(info_plist_path, 'rb') as fp:
    pl = plistlib.load(fp)

old_bundle_id = pl['CFBundleIdentifier']
print("Current Bundle-ID:", old_bundle_id)
old_version = pl['CFBundleShortVersionString']
print("Current App-Version:", old_version)

shutil.rmtree(payload_path)
os.rename(zip_path, ipa_path)

dateien_liste = []

tweaks_path = os.path.join(path, "tweaks")

for root, dirs, files in os.walk(tweaks_path):
    for dir in dirs:
        if old_bundle_id in dir:
            dir_path = os.path.join(tweaks_path, dir)
            dateien_liste.append(dir_path)

file_paths = []
for dir_path in dateien_liste:
    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)
        file_paths.append(item_path)


inject_this = ' '.join(['"' + item + '"' for item in file_paths])

file_name_no_ipa_with_extension = file_name_no_ipa + ".ipa"

modded_ipa_path = os.path.join(path, "modded_iPA", f"{old_bundle_id}_{old_version}")

pyzule_command = f'pyzule -o "{modded_ipa_path}" -i "{os.path.join(path, "decrypted_iPA", file_name_no_ipa_with_extension)}" -f {inject_this} -c 9'
subprocess.call(pyzule_command, shell=True)
