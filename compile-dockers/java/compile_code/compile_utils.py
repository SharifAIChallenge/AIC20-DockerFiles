import zipfile
import os, glob
import subprocess
import shutil
from subprocess import PIPE

def unzip(src, dest):
    """extracts zip file from source dierctory to destination directory.

        :param src: source folder path containing zip file.
        :param dest: destination folder for extract.
    """
    zip_ref = zipfile.ZipFile(src, 'r')
    zip_ref.extractall(dest)
    zip_ref.close()


def copy_from_root(src, dest, search_for, directory_index):
    """finds unzipped files root directory and copies it to destination directory.

        :param src: source directory containing unzipped files.
        :param dest: destination directory to paste code in.
        :param search_for: file name that the code must contain.
        :param directory_index: from search_for file how many directory levels
        you have to step back.
    """
    source_code_main = glob.glob(src + '/**/' + search_for, recursive=True)

    if len(source_code_main) == 0:
        raise Exception('File %s not found in the uploaded code.' % search_for)

    source_code_main = source_code_main[0][len(src):].strip('/')
    source_code_main_path = source_code_main.split('/')

    source_code_main_root = '/'.join(source_code_main_path[:directory_index])

    shutil.copytree(src + '/' + source_code_main_root, dest)


def remove_files_with_extention(src, extention):
    """removes all files in directory with exact extention.

        :param src: source directory to clean.
        :param extention: extention to delete.
    """
    extfiles = glob.glob(src + '/**/*.' + extention, recursive=True)
    for extfile in extfiles:
        os.remove(extfile)


def compile_java(src):
    """compile java code in directory.

        :param src: source directory containing java code.
    """

    try:
        subprocess.check_output('javac -Xlint:unchecked -classpath \'' +
            src + ':' + src + '/src:' + src + '/libs/gson-2.3.1.jar\' ' +
            src + '/src/client/Main.java', stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as failed:
        raise Exception('Compile failed with message: %s.' % failed.output.decode('utf-8'))


def recursively_change_owner(dir, new_owner):
    os.chown(dir, new_owner, new_owner)
    for root, dirs, files in os.walk(dir):
        for d in dirs:
            os.chown(os.path.join(root, d), new_owner, new_owner)
        for f in files:
            os.chown(os.path.join(root, f), new_owner, new_owner)