# File: homework2.py

# Your file path should look like:
# python_decal_fa25/yourname/homework2/homework2.py

# Questions (Answer these in the homework2.py file as comments):

# 1) What’s the difference between Git, GitHub, and Git Bash?

	# Git is a version control system analogous to a "cloud."
	# GitHub is a hosting platform for remotely storing and sharing Git projectsy.
	# Git Bash is a program that comes initiallized with Git and installs the "Bash" Shell Language. 

# 2) What’s the difference between the terminal and the command line?

	# Terminal is the text-based application that is programmed to the relavent shell.
	# Command line is within the terminal where commands are typed.

# 3) How does Windows PowerShell differ from Git Bash?

	# Windows PowerShell is the default terminal on Windows with the shell language Powershell, whereas Git Bash
	# is an alternative application that offers the Bash Shell (Unix based shell) and comes preinstalled with Git.  

# 4) What’s the difference between Anaconda, conda, and Python?

	# Anaconda is a distribution with many python packages.
	# Conda is package and environment manager.
	# Python is a scripting language.

# 5) What is VS Code? 

	# VS Code is an IDE (code editor & compiler)

# 6) What is a Jupyter Notebook? How is it different from Jupyter Lab?

	# A Jupyter notebook is a file of type .ipynb that allows for both markdown and code cells.
	# Jupyter Lab is an interactive development environment for Jupyter notebooks.

# 7) What does ~/ mean?

	# ~/ is short for the Home Directory. Ex: /Users/derek/

# 8) What’s the difference between an absolute path and a relative path?

	# The absolute is the full path starting with the root directory (ex: /Users/derek/python_decal_fa26)
	# The relative path depends on what directory you're currently in and omits the parent directorie(s) (ex: if in ~/ then only python_decal_fa26/
	# would have to be called

# 9) Imagine you're in your "yourname" repo. Write the absolute and relative paths to "course_assignments/homework2".

	# absolute path: Users/derek/python_decal_fa26/course_assignmignments/homework2
	# relative path: ../course_assignments/homework2

# 10) What command lets you move from "course_assignments/homework2/" to "course_assignments/"?

	# "cd .." (change to parent directory)

# 11) What would rm ./ do in your current directory? (Don’t try it!)

	# "rm ./" would remove all contents within the curent directory.

# 12) What do the following commands do?
# git add
# git commit
# git push

	# git add: adds file(s) to staging area
	# git commit:  commits file(s) to version history
	# git push: pushes commit(s) to remote repository (GitHub for our purposes)

# 13) What's the difference between "git add ." and "git add <file>"?

	# "git add .": adds contents of current repository. 
	# "git add <file>": adds specific <file> only.

# 14) What do "git status" and "git log -1" do?

	# git status: checks the status of a repo / gives a report on what git sees within the repo.
	# git log -1: shows only the most recent commit. 

# 15) What’s the difference between cloning a repository and pulling from it?

	# Cloning a repository downloads a local copy of it. Git pull updates a local copy with any new changes made to the remote repo.  

# 16) What has been your most frustrating bug or error in this class so far? How did you troubleshoot or fix it?

	# Havn't experienced any bugs yet. However, I commonly misspell or use "/" before a shell command (used to LaTeX) and get syntax errors.

# 17) What’s a question you still have? What’s something you’re confused about?

	# Why does Python not have an array datatype, rather needing to import numpy to use an np.array? 

# 18) Tell me a fun fact!

	# I used to have a "pet" squirrel named Squirreline Dione. 

# 19) Print your favorite math expression you've learned in Python so far. 
# (Hint: Use print() and add a comment explaining what it does.)

print(2.718 ** (1j * 3.14) + 1, "equals zero (almost)") # calculates e^iπ + 1 (e and π approximated) followed by the string "equals zero (almost)"
