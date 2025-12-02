# Github notes

.gitignore file is used to ignore files that you don't want to push to github.

Common files to include in .gitignore:
- __pycache__/
- **.env** - api keys (always and compulsory)
- **venv** - virtual environment folder (put the file name)

## Troubleshoot
If you accidentally push a file that should be in .gitignore, you can remove it from the repository by just deleting the **.git** folder and then reinitializing the repository.

Commands to commit

```bash
git init    
git add .
git commit -m "initial commit"
git branch -M main
git remote add origin <your-repo-link>
git push -u origin main
``` 

To push changes after the initial commit

```bash 
git add .
git commit -m "your message"
git push
```

