## Configuration file (secrets.ini)
The secrets.ini contains all of your personal credentials, API keys and the host names of all apps.  Without this file, tests will not run.

#### When adding a new field to the secrets file
1. Add the field to secrets.ini
2. In the resources/private/config.py, add a variable and link that to the new field of secrets.ini

#### Set up
1. Create a secrets.ini file in `resources/private/`
2. Make sure each field is properly filled out
3. Install the dependencies:

    <code>
        pip3 install -r requirements.txt
    </code>

## Set up environment
1. Install Python 3: https://www.python.org/downloads/
2. Add chrome driver to path e.g. `export PATH=$HOME/path_to_your_code/automation-test-framework-python/resources/chromedriver:$PATH`
3. Add Python path e.g. `export PYTHONPATH=$HOME/path_to_your_code/automation-test-framework-python`
4. Add Python path to path e.g. `export PATH=$PYTHONPATH:$PATH`