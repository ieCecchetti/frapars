# FRAPARS (France-parse-addresses)

Simple script that permits to parse addresses in France format.

## Install

To install, from the main proj folder, follows this steps:

1. Visit the [Poetry website](https://python-poetry.org/) to download the installer for your operating system.
2. Run the installer according to the instructions provided for your operating system.
3. After installation, verify that Poetry is installed correctly by opening a terminal or command prompt and typing:

```bash
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

```bash
poetry run script
```

## To execute tests

Just type in the terminal:

```bash
poetry run pytest
```

## Example

An example of the parser can be resumed here with this log:

```text
Initial address is: 100 Rue Chapelle
Result is: 100 Rue Chapelle 
Details: {'urba_names': ['rue'], 'prepositions': [], 'city': [], 'address_num': ['100'], 'department': [], 'street_name': ['chapelle']}
Unparsed string remained is: 
Parse quality scored: 1.0
-------------------------------------------
Initial address is: 100 Rue Colombes (De)
Result is: 100 Rue De Colombes 
Details: {'urba_names': ['rue'], 'prepositions': ['de'], 'city': ['colombes'], 'address_num': ['100'], 'department': [], 'street_name': []}
Unparsed string remained is: 
Parse quality scored: 1.0
```

The script runned with `poetry run dev` can execute in 3 different ways:

### Single address

with the command:

`poetry run dev -a "Rue, Saint-Philippe 31 (De)"`

```text
Fra-parse 0.2.0
Developed by eCecchetti
Initial address is: Rue, Saint-Philippe 31 (De)
Result is: 31 Rue De Saint Philippe 
Details: {'urba_names': ['rue'], 'prepositions': ['de'], 'city': [], 'address_num': ['31'], 'department': [], 'street_name': ['saint philippe']}
Unparsed string remained is: ,
Parse quality scored: 0.98
Process has finished!
```

### List of addresses

with the command:

`poetry run dev -l "Rue, Saint-Philippe 31 (De); Saint Marcelle (De) Avenue 32 10141"`

```text
Fra-parse 0.2.0
Developed by eCecchetti
Processing: 100%|████████████████████████████████████████████████| 2/2 [00:00<00:00, 134.66item/s]
Unparsed: Rue, Saint-Philippe 31 (De) --> Parsed: 31 Rue De Saint Philippe
Unparsed:  Saint Marcelle (De) Avenue 32 10141 --> Parsed: 32 Avenue De Saint Marcelle 10141
Process has finished!
```

### File conversion

with the command:

`poetry run dev -i "your/file/path/filename.csv"`

```text
Fra-parse 0.2.0
Developed by eCecchetti
Found 234253 addresses to parse
Processing: 100%|████████████████████████████████████████████████| 234253/234253 [27:18<00:00, 142.99item/s]
Storing into file the results
Result printed at:  frapars/res/parsed_addresses.csv
Process has finished!
```

## To-Do List

- [ ] Write junit tests
- [ ] More example
- [ ] Update insee file - create a task that do it 

Enjoy and Rate!!
