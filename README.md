Early prototype of an Eve program.
It uses Python, EsiPy, PostgreSQL. xlwings used to output data to Excel in a human readable form.

What currently works:
    - SSO (eve_sso.py) reads and writes tokens and codes correctly according to ESI documentation.
    - Can be used to pull information from API with authorization
    - Establishes connection to a PostgreSQL database
    - A simple Cache implemented to speedup SSO process

What does not:
    - The program itself (main.py), due to a refactor in progress.
    - Refactor a monkeypatch for update function of EsiPy to use the absolute expiry date from verify() instead, and
      other things to make authorization as efficient as possible.
    - Storage of json tokens in ini is bad for readability, needs to be refactored, although it does work.
    - No output to Excel yet, because of the above
    - SDE database not implemented