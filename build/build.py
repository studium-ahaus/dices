import os
import shutil

thisDir: str = os.path.dirname(os.path.realpath(__file__))
targetFile: str = thisDir + '/dices'

if os.path.exists(targetFile):
    os.remove(targetFile)

shutil.make_archive(targetFile, 'zip', thisDir + '/../src')
