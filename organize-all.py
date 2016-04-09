import zipfile
import glob
import re
import os
import shutil
import csv

students = {}


def isdir(z, name):
  return any(x.startswith("%s/" % name.rstrip("/")) for x in z.namelist())


def parse_students(filename):
  with open(filename, 'rb') as student_list:
    reader = csv.reader(student_list)
    for row in reader:
      students[row[1]] = {'name': row[0], 'canvas_id': row[
          1], 'uni': row[2], 'is_late': False}

def unzip_batch():
  batches = glob.glob('original-submissions/*.zip')
  for batch in batches:
    with zipfile.ZipFile(open(batch, 'rb')) as batch_zip:
      batch_zip.extractall('./originals/')


def organize():
  submissions = glob.glob('originals/*.zip')
  for submission_zip_filename in submissions:
    with zipfile.ZipFile(open(submission_zip_filename, 'rb')) as submission_zip:
      user_details = re.search(
          '([a-z]+)_([0-9]+)', submission_zip_filename.lower())
      student = students[user_details.group(2)]

      late_flag = re.search('_late_', submission_zip_filename.lower())
      is_late = late_flag != None

      folder_name = '%s %s' % (student['uni'], student['name'])
      if is_late:
        folder_name = '%s (Late)' % folder_name
        student['is_late'] = True

      folder_name = os.path.join('./submissions_all', folder_name)
      if not os.path.exists(folder_name):
        os.makedirs(folder_name)

      # stupid Mac OSX. remove hidden files
      java_files = [filename for filename in submission_zip.namelist(
      ) if '__MACOSX' not in filename]
      java_files = [
          filename for filename in java_files if not isdir(submission_zip, filename)]

      for java_file in java_files:
        source = submission_zip.open(java_file)
        target = file(os.path.join(
            folder_name, os.path.basename(java_file)), 'wb')
        with source, target:
          shutil.copyfileobj(source, target)


student_name_files = glob.glob('gradebook-downloads/*.csv')
for student_name_file in student_name_files:
  parse_students(student_name_file)

unzip_batch()
organize()
