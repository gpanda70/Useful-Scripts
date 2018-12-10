import os
from datetime import datetime
from zipfile import ZipFile
from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory

"""

This program can either Zip or Unzip files from a directory and place them in
any output directory of your choosing.
Note if a subdirectory is empty it won't be zipped.
"""


class NoPathChosen(Exception):
    pass

class Zipper:
    """
    This Class directly zips contents inside a folder and stores them
    in folders
    """

    def __init__(self, input_path='', output_path=''):
        """Default constructor to read in variables"""
        self.input_path = input_path
        self.output_path = output_path
        self.base_input_folder = os.path.basename(input_path)

        self.zipfile_name = self._name_zipfile()
        self.zipfile_path = os.path.join(self.output_path, self.zipfile_name)
        self.zf = ZipFile(self.zipfile_path, 'w')

    def from_tkinter(self):
        """Second constructor used to read in using tkinter"""
        # I add this to remove additional window that opens with askopenfolder
        Tk().withdraw()
        self.input_path = askdirectory(title="Choose the folder whose content you want to zip")
        self.output_path = askdirectory(title="Choose the folder where you want to save your zip file")
        self.base_input_folder = os.path.basename(self.input_path)

        self.zipfile_name = self._name_zipfile()
        self.zipfile_path = os.path.join(self.output_path, self.zipfile_name)
        self.zf = ZipFile(self.zipfile_path, 'w')

    def zip_folder(self):
        """
        This function zips the base input folder at your given output path
        """

        if not (self.input_path and self.output_path):
            raise NoPathChosen('Either your input path or output path is empty')

        # Traverses through your chosen folder path to zip all the files
        for input_root, input_dir, input_files in os.walk(self.input_path):
            for input_file in input_files:
                print(input_root)
                print(input_dir)
                self._write_to_zipfile_path(input_root, input_dir, input_file)

    def _name_zipfile(self):
        """
        Combines the folder name with the information you want to zip,
        and new zip file name to create new zipname.
        """
        today_date = datetime.now().strftime('%Y.%m.%d')
        zipfile_name = '{}_{}.zip'.format(today_date, self.base_input_folder)
        return zipfile_name

    def _write_to_zipfile_path(self, root, dir, file):
        """
        Uses ZipFile object to zip file to new zipfile_path.
        """

        # Prevents the zip file from adding itself to the archive
        if file != os.path.basename(self.zipfile_path):
            file_path = os.path.join(root, file)  # The full file path
            file_rel_path = os.path.relpath(file_path, self.input_path)
            self.zf.write(file_path, file_rel_path)


if __name__ == "__main__":
    print('Zipping...')
    zipper = Zipper()
    zipper.from_tkinter()
    zipper.zip_folder()
    print('Done!')
