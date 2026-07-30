import shutil

if "{{ cookiecutter.use_snakemake }}" == "no":
    shutil.rmtree("workflow", ignore_errors=True)
    shutil.rmtree("config", ignore_errors=True)

help = """
Your project has been created!
_____________________________________________________________________________
                            ___________ _
  \/                    __/   .::::.-'-(/-/)
                     _/:  .::::.-' .-'\/\_`*******            __ (_))
        \/          /:  .::::./   -._-.  d\|                 (_))_(__))
                     /: ("'"'/    '.  (__/||             (_))__(_))--(__))
                      \::).-'  -._  \/ \\/\|
              __ _ .-'`)/  '-'. . '. |  (i_O
          .-'      \       -'      '\|
     _ _./      .-'|       '.  (    \\                           % % %
  .-'   :      '_  \         '-'\  /|/      @ @ @               % % % %
 /      )\_      '- )_________.-|_/^\      @ @ @@@             % %\/% %
 (   .-'   )-._-:  /        \(/\'-._ `.     @|@@@@@              ..|........
  (   )  _//_/|:  /          `\()   `\_\     |/_@@               )'-._.-._.-
   ( (   \()^_/)_/             )/      \\    /                  /   /
    )  _.-\\.\(_)__._.-'-.-'-.//_.-'-.-.)\-'/._                /       
.-.-.-'   _o\ \\\     '::'   (o_ '-.-' |__\'-.-;~ ~ ~ ~ ~ ~ ~~/   /\   
          \ /  \\\__          )_\    .:::::::.-'\            '- - -|
     :::''':::::^)__\:::::::::::::::::'''''''-.  \                  '- - - - 
    :::::::  '''''''''''   ''''''''''''':::. -'\  \       C. SWANSIGER
_____':::::_____________________________________\__\_________________________

If you have not done so already, create a conda environment for your new 
project. A basic environment.yml file has been created for you, so the
following should work:

cd {{cookiecutter.repo_name}}
conda env create -f environment.yml
conda activate {{cookiecutter.package_name}}

If you would like to specify your own environment, you can do the following:

cd {{cookiecutter.repo_name}}
conda env create --name {{cookiecutter.repo_name}} python={{cookiecutter.python_version}}
conda activate {{cookiecutter.repo_name}}
conda env export > environment.yml

Install your new project in your local conda environment with:

pip install -e .

Files placed under data/ are ignored by git by default (except for the
README.md placeholders) so they won't sync to version control.
{% if cookiecutter.use_snakemake == "yes" %}
A Snakemake skeleton has been set up under workflow/ and config/. Add rules
under workflow/rules/, then run the pipeline with:

snakemake --cores all
{% endif %}
!!! Update the author information in pyproject.toml !!!

Don't forget to sync to GitHub. Have fun!
"""
print(help)
