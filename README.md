# Smartsheet BIC Recreational
======
Downloads the current Smartsheet Bic Open Task List
Can specificy a ```--name``` for the output file.

# Installing
```
git clone git@github.com:northriverboats/smartsheet_total_rec_boat_sales.git
cd smartsheet_total_rec_boat_sales
# setup and activate venv

python -m pip install --upgrade pip
pip install git+https://github.com/northriverboats/emailer.git
pip install -r requirements

# edit .env file
cp env.sample .env
```

# Creating Executable
File will be in ```builds``` folder
```
pyinstaller smartsheet_bic_open_task_list.spec
```
