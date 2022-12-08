# LightHouse

LightHouse is a rather simple and straightforward file integrity monitoring tool. This utility can recognize, record, and report file creation, deletion, and content changes. At the instance of a infraction, LightHouse will inform the user via email while generating logs about the event.

Features : 

Detecting
- any changes made to contents of a file
- any new files that were added to the directory
- renaming of a file
- removal or deletion of a file

Multiple filter options to exclude selected files or directories from the monitoring scope

Concentrate on monitoring a single file or multiple files

Generates logs and sends the report to the user via email


## Prerequisites

- Python 3 or later

## Installation guide and Usage

- First, clone the project files to a directory that has write permissions enabled. This directory should be outside the directories that the you intend to monitor. The necessary settings and variations can be done by editing the "settings.py" file. To start monitoring, copy the paths of the files and directories that needs monitoring into the "watch_list.txt", each on a new line.

The single file monitoring format is as follows:
```
/var/www/html/jets.php
```

The directory monitoring format is as follows which consists of the order:


- directory path, state "true" or "false"  to specify if subdirectories needs to be monitored as well, files extensions that needs to be excluded from the monitoring process separated by "|", the maximum file size in bytes.

```
/var/www/html/wordpress/wp-content/themes, false, .css|.woff|.ttf, 1048576

/var/www/html/wordpress/wp-content/themes, true, .css, 1048576

/var/www/html/wordpress/wp-content/themes, true, .css
```

Run the script 'watchtower.py' with silent-scan option:

```
python3 lighthouse.py --silent-scan
```
-The watch list file (watch_list.txt) will be scanned via the quiet scan option, which will also record the files. There won't be any notifications or alarms set off. Every time you add new files to the folders being monitored, use this option.

Make a cron job to perform regular scanning. Every minute, the following cron will run. According to your needs, adjust.

```
$ crontab -e
# append the following line, adjust project path

* * * * * python3 /opt/file_watchtower/watchtower.py --routine_scan
* * * * * python3 /opt/file_watchtower/watchtower.py --process-email-queue
```
## Command Line Args






