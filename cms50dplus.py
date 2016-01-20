#!/usr/bin/env python
import sys, serial, argparse, csv, datetime
from dateutil import parser as dateparser
import cms50dplus

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="cms50dplus.py v1.2 - Contec CMS50D+ Data Downloader (c) 2015 atbrask")
    parser.add_argument("mode", help="Specify LIVE for live data or RECORDED for recorded data.", choices=["LIVE", "RECORDED"])
    parser.add_argument("serialport", help="The device's virtual serial port.")
    parser.add_argument("output", help="Output CSV file.")
    parser.add_argument('-s', "--starttime", help="The start time for RECORDED mode data.", type=cms50dplus.valid_datetime)

    args = parser.parse_args()

    if args.mode == 'LIVE':
        cms50dplus.dumpLiveData(args.serialport, args.output)
    elif args.mode == 'RECORDED' and args.starttime is not None:
        cms50dplus.dumpRecordedData(args.starttime, args.serialport, args.output)
    else:
        print "Missing start time for RECORDED mode."

    print ""
    print "Done."
