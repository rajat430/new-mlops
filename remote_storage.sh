# dvc init
git add .dvc .dvcignore
git commit -m "init dvc"
dvc add data/raw/
git commit -m "track dataset with dvc"
dvc remote add -d myremote azure://data
dvc remote modify myremote account_name 'mystorage0101010101011'
dvc remote modify --local myremote account_key ''