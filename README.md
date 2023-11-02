# automatic-tweaked-iPA-updater

## Description
This Python script is designed to automate the process of updating .iPA files. It unzips the .iPA files, extracts the necessary information, injects tweaks, and repackages them.

## Dependencies
This script requires Python 3 and the following Python libraries:
- os
- zipfile
- time
- sys
- plistlib
- shutil
- subprocess

In addition, it requires the `pyzule` command-line tool to inject tweaks into the .iPA files.

## Installation
1. Ensure that you have Python 3 installed on your system. You can download it from the official Python website.
2. Install the required Python libraries. If you have pip (Python's package installer) installed, you can do this by running `pip install os zipfile time sys plistlib shutil subprocess` in your command line.
3. Download and install `pyzule` from its official repository.
4. Clone this repository or download the script to your local machine.

## Usage
1. Store your .iPA files in the 'decrypted_iPA' folder.
2. Run the script using Python by typing `python <script_name>.py` in your command line.
3. The script will process all .iPA files in the 'decrypted_iPA' folder one by one, injecting tweaks and repackaging them.
4. The updated .iPA files will be stored in the 'modded_iPA' folder.

Please note that folders in the 'tweaks' directory should be named as follows: `<desired name of tweaked iPA (e.g., Flightradar Gold or YouTube OLED)> | <bundle ID of the app into which tweaks are to be injected>`

<p align="center">
  <img src="https://github.com/binnichtaktiv/automatic-tweaked-iPA-updater/assets/96953964/cbae0985-9d87-4b89-91f0-505d55bcfe46" width="400" alt="Screenshot">
</p>
