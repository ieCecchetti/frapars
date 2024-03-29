# FRA-P-ADRS
Simple script that permits to parse addresses in France format.

# Install
To install, from the main proj folder, follows this steps:
```bash
# create virtual env
python -m venv .venv
source .venv/bin/activate
pip install -r requirement.txt
```
Then you are ready to launch it!

# To run
Execute simply the script by
```
python script.py
```

# To-Do List
- [ ] Publish in git
- [ ] Clean structure (use maybe poetry)
- [ ] Create a simple init graphic
- [ ] Add args and helper: [`single_address`, `csv`]
- [ ] Split the csv in piece and execute in more thread  (to fasten up)
- [ ] Write junit tests
- [ ] Create package for pypi to be imported
- [ ] Dockerize ?
- [ ] Re-download the insee.csv when is old (every month)
