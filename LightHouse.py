__author__ = "O. K. Siriwardena & Maneesha K. D. H."
__license__ = "GNU General Public License v2.0"
__version__ = "1.0"
__email__ = "it20058050@my.sliit.lk"
__created__ = "16/Oct/2022"
__modified__ = "23/Oct/2022"
__project_page__ = "https://github.com/IT20058050/oshxn"


import argparse
import sys
import LightHouse_core
import db
import notifier

arg_parser = None


def run(args):

    if args['routine_scan']:
        LightHouse_core.start_scan(False)
    elif args['silent_scan']:
        LightHouse_core.start_scan(True)
    elif args['process_email_queue']:
        notifier.send_queued_messages()
    elif args["export_db"]:
        export_path = input("Enter the output path: ")
        LightHouse_core.export_file_records_to_csv(export_path)
    elif args["reset"]:
        ans = input("WARNING: This will delete all database records. Do you really want to continue [Y/N]? ")
        if ans.upper() == "Y":
            db.delete_all_data()
            print("Database has been cleared.")
        else:
            sys.exit()
    else:
        arg_parser.print_help()
        sys.exit()

def generate_argparser():

    ascii_logo = """
  ______  _  _         _       _         _      _    _    _                           
 |  ____|(_)| |       | |     (_)       | |    | |  | |  | |                          
 | |__    _ | |  ___  | |      _   __ _ | |__  | |_ | |__| |  ___   _   _  ___   ___  
 |  __|  | || | / _ \ | |     | | / _` || '_ \ | __||  __  | / _ \ | | | |/ __| / _ \ 
 | |     | || ||  __/ | |____ | || (_| || | | || |_ | |  | || (_) || |_| |\__ \|  __/ 
 |_|     |_||_| \___| |______||_| \__, ||_| |_| \__||_|  |_| \___/  \__,_||___/ \___| 
                                   __/ |                                              
                                  |___/                                               
 
    
    Simple File Integrity Monitoring Tool

    https://github.com/IT20058050/oshxn
    """
    ap = argparse.ArgumentParser(ascii_logo)

    ap.add_argument("-r", "--routine-scan", action='store_true',
                    help="This is the general scan, normally executed by the OS cron manager."
                         "The routine scan type scans and reports changes that happens to the directories or files that are being watched")

    ap.add_argument("-s", "--silent-scan", action='store_true',
                    help="This silent scan will parse the watch list file (watch_list.txt) to create a record of the file(s) displaying alerts. It is recommended to do execute this whenever changes are made items in the watch list.")

    ap.add_argument("-e", "--process-email-queue", action='store_true',
                    help="Send pending email notifications")

    ap.add_argument("--export-db", action='store_true',
                    help="Generate a CSV file of the database file records.")

    ap.add_argument("--reset", action='store_true',
                    help="Clear out the file records database.")

    ap.add_argument("--version", action="version", version='File LightHouse Version 1.0')

    return ap


def main():
    global arg_parser
    arg_parser = generate_argparser()

    args = vars(arg_parser.parse_args())
    run(args)


if __name__ == "__main__":
    main()
