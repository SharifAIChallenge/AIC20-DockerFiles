import glob
import shutil
import json
import compile_utils
import os

root_dir = '/compile'

source_dir = root_dir + '/code.zip'
unzipped_dir = root_dir + '/unzipped'
compile_dir = root_dir + '/compiled/code/src'
log_dir = root_dir + '/log'

errors = []
stage = -1

try:

    # unzip the code
    stage = 0
    compile_utils.unzip(source_dir, unzipped_dir)

    # remove existing compilation results
    stage = 1
    shutil.rmtree(compile_dir, ignore_errors=True)

    # find main.cpp and copy the root
    stage = 2
    compile_utils.copy_from_root(unzipped_dir, compile_dir, 'main.cpp', -1)

    # compile

    current_uid = os.geteuid()
    compile_utils.recursively_change_owner(compile_dir, 2016)
    os.seteuid(2016)

    stage = 3
    try:
        compile_utils.compile_cpp(compile_dir)
    finally:
        os.seteuid(current_uid)
        os.chown(compile_dir, current_uid, current_uid)

    # make archive
    stage = 4
    shutil.copy2( '/utils/run.sh' , '/compiled/code/' )
    shutil.make_archive(root_dir + '/compiled/compiled', 'zip', '/compiled/code/')

    # remove compilation results
    stage = 5
    shutil.rmtree(compile_dir, ignore_errors=True)

    stage = 6

except Exception as e:

    errors = e.args


with open(log_dir + '/status.log', 'w') as logfile:
    json.dump({'stage': stage, 'errors': errors}, logfile)
