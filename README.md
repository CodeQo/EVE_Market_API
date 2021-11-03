Codes requires extensive cleanup for readability. Currently a scrap paper. 

# Eve Market
Early prototype of an Eve program. Pulls automated and authorized requests with ESI (Eve's API) from the game's servers.

## Goal
Excel is great for simple usage, but current SSO requirements are too strict for standalone usage of Excel's PowerQuery. 
* A full-scale program to pull market, personal assets and everything required for individual tax, reprocessing and manufacturing calculations at regular intervals. 
* Assessment of profitability in production chains with multiple steps.
 
### Short-term goals
* Auto check and compare best sell price for assets in a (given) station inventory for nearby regions. 
* Calculate appropriate prices for more uncommon market listings of raw ore before reprocessing, normalizing it to market values of base ores.

### Mid-term
* Production chain: With a given sales price, existing materials and their market value, calculate the room to negotiate in individual contracts.
* Data modelling: With Eve's currently more volatile approach to economy, a way to view how much influence ore has on the end-price to respond swiftly to changes, especially in unsold products. This will need extensive use of SDE. 

### Long-term outline
* In a future implimentation automated e-mail alerts when prices reach given thresholds.

## Backbone 
It uses Python, EsiPy, PostgreSQL. xlwings used to output data to Excel in a human readable form.

###What currently works:
* SSO (eve_sso.py) reads and writes tokens and codes correctly according to ESI documentation.
* Can be used to pull information from API with authorization
* Establishes connection to a PostgreSQL database
* A simple Cache implemented to speedup SSO process

###What does not:
* The program itself (main.py), due to a refactor in progress.
* Refactor a monkeypatch for update function of EsiPy to use the absolute expiry date from verify() instead, andother things to make authorization as efficient as possible.
* Storage of json tokens in ini is bad for readability, needs to be refactored, although it does work.
* No output to Excel yet, because of the above
* SDE database not implemented
