#remove existing dvc config and initialize dvc
rm -rf .dvc
rm -f .dvcignore
rm dvc.lock
#Initialize dvc and track the dataset with dvc

dvc init
git add .dvc .dvcignore
git commit -m "init dvc"
dvc add data/raw/
git commit -m "track dataset with dvc"
dvc remote add -d myremote azure://data
dvc remote modify myremote account_name 'mystorage0101010101011'
dvc remote modify --local myremote account_key "$SECRETS"
dvc repro
dvc push
git add .
git commit -m "push dataset to remote storage"
git push