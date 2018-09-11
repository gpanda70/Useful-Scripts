import os
from datetime import datetime
from zipfile import ZipFile
from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory

"""

This program zips one or more directories and names it using today's date

"""

today = datetime.now().strftime('%Y.%m.%d')
Tk().withdraw()  # I add this to remove additional window that opens with askopenfilename()
folder_path = askdirectory()
folder_name = folder_path.split(r'/')[-1]
output_path = askdirectory()

def zip_folder(fp, fn, op):
    """
    This function zips the chosen folder at your given output path

    Keyword Arguments:
    fp(str) -- Folder Path
    fn(str) -- Folder Name
    op(str) -- Output Path

    Returns: None
    """

    zip_path = os.path.join(op, today + '_' + fn + '.zip')  # path of the zip file
    zf = ZipFile(os.path.join(zip_path), 'w')

    for root, dir, files in os.walk(fp):
        for file in files:
            """Prevents the zip file from adding itself to the archive"""
            if file != os.path.basename(zip_path):
                file_path = os.path.join(root,file)
                zf.write(file_path, os.path.basename(file_path))


if __name__ == "__main__":
    print('Zipping...')
    zip_folder(folder_path, folder_name, output_path)
    print('Done!')
