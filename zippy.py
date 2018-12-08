import os
from datetime import datetime
from zipfile import ZipFile
from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory

"""

This program can either Zip or Unzip files and place them in any directory of
your choosing

"""


class Zipper:
    """
    This Class directly zips contents inside a folder and stores them
    in folders
    """

    def __init__(self, input_path, output_path):
        """Default constructor to read in variables"""
        self.input_path = input_path
        self.output_path = output_path
        self.base_input_folder = os.path.basename(input_path)

    @classmethod
    def from_tkinter(cls):
        """Second constructor used to read in using tkinter"""
        # I add this to remove additional window that opens with askopenfolder
        Tk().withdraw()
        input_path = askdirectory(title="Choose the folder whose content you want to zip")
        output_path = askdirectory(title="Choose the folder where you want to save your zip file")
        base_input_folder = os.path.basename(input_path)
        return cls(input_path, output_path, base_input_folder)

    def zip_folder(self):
        """
        This function zips the base input folder at your given output path

        Keyword Arguments:
        fp(str) -- Folder Path
        fn(str) -- Folder Name
        op(str) -- Output Path

        Returns: None
        """
        zipfile_name = self.name_zipfile()  # zip name
        zip_path = os.path.join(self.output_path, zipfile_name)

        # Traverses through your chosen folder path to zip all the files
        for input_root, input_dir, input_files in os.walk(self.input_path):
            for input_file in input_files:
                self.write_to_zip_path(input_root, input_file, zip_path)

    def name_zipfile(self):
        """
        Combines the folder name with the information you want to zip,
        and new zip file name to create new zipname.
        """
        today_date = datetime.now().strftime('%Y.%m.%d')
        new_name = '{}_{}.zip'.format(today_date, self.base_input_folder)
        return new_name

    def write_to_zip_path(self, root, file, zip_path):
        """
        Uses ZipFile object to zip file to new zip_path.
        """
        zf = ZipFile(zip_path, 'w')
        # Prevents the zip file from adding itself to the archive
        if file != os.path.basename(zip_path):
            file_path = os.path.join(root, file)
            zf.write(file_path, os.path.basename(file_path))


if __name__ == "__main__":
    print('Zipping...')
    zipper = Zipper.from_tkinter()
    zipper.zip_folder()
    print('Done!')
