# Canvas Homework Submission Organizer

Extracts and organizes downloaded assignments by UNI.

## Quick Start

1. Go to the *Grades* page on *Canvas* and export the the current grades of all students in the class. Put this `.csv` into the `gradebook-downloads` folder. This is used to cross reference `UNI`s from Canvas' annoying `user_id`.
2. Go to the *Assignments* page, select the assignment that you want, and click on *Download Submissions*. You'll end up downloading a `.zip` file containing the zipped submissions of all students. Don't unzip it. Just throw the single batch zip file into `original-submissions`
3. `python organize-all.py`

This would create:

1. A folder `originals` that contains the zips for each student
2. A folder `submissions_all` that contains the submissions for each student as organized by their `UNI`. This would also put all the students' files in the directory, ignoring whatever weird directory structure that students tend to submit their work in.

You can do this for multiple classes too. Just put as many `.csv`s into `gradebook-dnwloads` as you want, and/or multiple `.zip`s in `original-submissions`.


