import os
import errno
import argparse

ENV_ARGS = {
    'HOME': os.getenv('HOME')
}
DELIMITER = '_!_'

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--force', help='Overrides existing files', action='store_true')

args = parser.parse_args()

for dir_name in os.listdir(path='.'):
    if dir_name.startswith('apply') and os.path.isdir(dir_name):
        for file_name in os.listdir(path=dir_name):
            settings_file_name = os.path.join(*file_name.format(**ENV_ARGS).split(DELIMITER))
            try:
                os.mkdir(os.path.dirname(settings_file_name))
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
            if args.force:
                try:
                    os.remove(settings_file_name)
                except OSError as e:
                    if e.errno != errno.ENOENT:
                        raise
            try:
                os.symlink(os.path.abspath(os.path.join(dir_name, file_name)), settings_file_name)
            except OSError as e:
                if e.errno == errno.ENOENT:
                    print(e)
                else:
                    raise
