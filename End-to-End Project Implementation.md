# Steps involved in implementing an end-to-end project

## GitHub Setup
* Create a new repo in GitHub.
* Create a new venv using the command `python -m venv ./<Name of Virtual Environment>`
* Activate the venv using the command `.\<Name of Directory>\Scripts\activate`
* Create a README.md file
* Follow the steps as mentioned in GitHub
    * `git add README.md`
    * `git commit -m "<Commit Message>"`
    * `git branch -M main`
    * `git remote add origin <URL of GitHub repo>`
    * `git push -u origin main`
* If making any changes in GitHub directly, make sure to use the `git pull` command to make sure that the IDE is in sync with GitHub.