import os
git_url=input("Enter the Git repository url: ")
os.system('git init')
os.system('git add .')
os.system('git status')
os.system('git commit -m "Initial commit"')
os.system('git remote add origin '+git_url)
os.system('git push -f origin master')
print("\n updation completed")