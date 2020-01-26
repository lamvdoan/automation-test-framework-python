## Configuration file (secrets.ini)
The secrets.ini contains all of your personal credentials, API keys and the host names of all apps.  Without this file, tests will not run.

#### When adding a new field to the secrets file
1. Add the field to secrets.ini
2. In the `resources/private/config.py`, add a variable and link that to the new field from secrets.ini

#### Set up
1. Install Python 3: https://www.python.org/downloads/
2. Create a secrets.ini file in `resources/private/`
3. Make sure each field is properly filled out
4. Install the dependencies:

    <code>
        pip3 install -r requirements.txt
    </code>
