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
* Use `git add .` to add all the changed/modified files.

## setup.py & requirements.txt
In Python, **setup.py** is a module used to build and distribute Python packages. It typically contains information about the package, such as its name, version, and dependencies, as well as instructions for building and installing the package. It basically allows us to create our machine learning project as a package.

* Also create a folder named `src`. Inside that, create a `__init__.py` file. Entire project development will be made inside the `src` folder
* Add `-e .` at the end of `requirements.txt` file. This will trigger the `setup.py` file.
* Now whenever we run the command `pip install -r requirements.txt`, the setup file will get triggered and the package will be built.