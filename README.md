# FRA-P-RS (France-parse-addresses)
Simple script that permits to parse addresses in France format.

## Install
To install, from the main proj folder, follows this steps:
1. Visit the [Poetry website](https://python-poetry.org/) to download the installer for your operating system.
2. Run the installer according to the instructions provided for your operating system.
3. After installation, verify that Poetry is installed correctly by opening a terminal or command prompt and typing:
```
poetry --version
```
This command should display the installed version of Poetry.
For more detailed installation instructions and usage guidelines, refer to the [Poetry Installation Guide](https://python-poetry.org/docs/).

Then for installing the project:
```bash
# in case you are using vscode: this will make vsCode recognise and create the .venv 
poetry config virtualenvs.in-project true
# create virtual env
poetry install
# activate the env
poetry shell
```
Then you are ready to launch it!

## To run
Just type in the terminal:
```
poetry run script
```

## To execute tests
Just type in the terminal:
```
poetry run pytest
```

## Example
An example of the parser can be resumed here with this log:
```text
Initial address is: 100 Rue Chapelle
Result is: 100 Rue Chapelle 
Details: {'urba_names': ['rue'], 'prepositions': [], 'city': [], 'addres_num': ['100'], 'department': [], 'street_name': ['chapelle']}
Unparsed string remained is: 
Parse quality scored: 1.0
-------------------------------------------
Initial address is: 100 Rue Colombes (De)
Result is: 100 Rue De Colombes 
Details: {'urba_names': ['rue'], 'prepositions': ['de'], 'city': ['colombes'], 'addres_num': ['100'], 'department': [], 'street_name': []}
Unparsed string remained is: 
Parse quality scored: 1.0
```

## To-Do List
- [x] Publish in git
- [x] Clean structure (use maybe poetry)
- [ ] Create a simple init graphic
- [ ] Add args and helper: [`single_address`, `csv`]
- [ ] Split the csv in piece and execute in more thread  (to fasten up)
- [ ] Write junit tests
- [ ] Create package for pypi to be imported
- [ ] Dockerize ?
- [ ] Re-download the insee.csv when is old (every month)
