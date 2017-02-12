import glob
import shutil
import json
import compile_utils
import os

root_dir = '/compile'
utils_dir = '/utils'

source_dir = root_dir + '/code.zip'
unzipped_dir = root_dir + '/unzipped'
compile_dir = root_dir + '/compiled/code/src'
log_dir = root_dir + '/log'

errors = []
stage = -1

try:
    # remove existing compilation results
    stage = 0
    shutil.rmtree(compile_dir, ignore_errors=True)

    # copy libs and project files
    stage = 1
    shutil.copytree(utils_dir + '/AIC16-Client-Java', compile_dir)

    # unzip the code
    stage = 2
    compile_utils.unzip(source_dir, unzipped_dir)

    # find and copy the root of the client
    stage = 3
    copy_done = compile_utils.copy_from_root(unzipped_dir, compile_dir + '/src', 'Controller.java', -2)

    # remove .class files
    stage = 4
    compile_utils.remove_files_with_extention(compile_dir, '.class')

    # compile
    stage = 5
    current_uid = os.geteuid()
    compile_utils.recursively_change_owner(compile_dir, 2016)
    os.seteuid(2016)

    stage = 5
    try:
        compile_done = compile_utils.compile_java(compile_dir)
    finally:
        os.seteuid(current_uid)
        os.chown(compile_dir, current_uid, current_uid)

    # make archive
    stage = 6
    shutil.copy2( '/utils/run.sh' , '/compiled/code/' )
    shutil.make_archive(root_dir + '/compiled/compiled', 'zip', '/compiled/code/')

    # remove compilation results
    stage = 7
    shutil.rmtree(compile_dir, ignore_errors=True)

    stage = 8

except Exception as e:

    errors = e.args


with open(log_dir + '/status.log', 'w') as logfile:
    json.dump({'stage': stage, 'errors': errors}, logfile)
