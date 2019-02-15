import zipfile
import sys
import os, glob
import shutil
import py_compile
import compileall
import io
from contextlib import redirect_stdout


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
    source_code_main =  glob.glob(src + '/**/' + search_for, recursive=True)

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


def compile_py3(src):
    """compile py3 code in directory.

        :param src: source directory containing java code.
    """
    
    pyfiles = glob.glob(src + '/**/*.py', recursive=True)
    for pyfile in pyfiles:
        try:
            py_compile.compile(pyfile, doraise=True)
        except py_compile.PyCompileError as py_error:
            raise Exception('Compile failed with message: %s.' % str(py_error))


def recursively_change_owner(dir, new_owner):
    os.chown(dir, new_owner, new_owner)
    for root, dirs, files in os.walk(dir):
        for d in dirs:
            os.chown(os.path.join(root, d), new_owner, new_owner)
        for f in files:
            os.chown(os.path.join(root, f), new_owner, new_owner)