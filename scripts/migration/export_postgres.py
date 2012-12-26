#!/usr/bin/env python

import argparse
import os
import subprocess

TABLES_TO_DUMP = [
    'auth_user',
    'main_anonymousstoryvote',
    'main_photoupload',
    'main_story',
    'main_userstoryvote',
]

def dump_table(table, fn):
    fn = os.path.abspath(fn)
    cmd = "COPY %s TO '%s' CSV FORCE QUOTE *" % (table, fn)
    subprocess.call(['psql', 'onlyat_django', '-c', cmd])

def main():
    parser = argparse.ArgumentParser(
        description = "Dump relevant tables from Only at Tech's postgres.")
    parser.add_argument('output_dir', metavar='output-dir',
                        help='A (non-existent) output directory for the script')
    args = parser.parse_args()

    if os.path.exists(args.output_dir):
        parser.error('Output directory exists, will not proceed.')

    os.mkdir(args.output_dir)

    for table in TABLES_TO_DUMP:
        dump_table(table, '%s/%s.csv' % (args.output_dir, table))

if __name__ == '__main__':
    main()
