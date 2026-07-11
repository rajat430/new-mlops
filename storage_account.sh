#!/bin/bash

set -e
az login
# =========================
# CONFIG
# =========================
LOCATION="eastus"
STORAGE_ACCOUNT_NAME="mystorage0101010101011"
CONTAINER_NAME="data"

# =========================
# STEP 1: Fetch Resource Group automatically
# (you can refine filter if needed)
# =========================
RESOURCE_GROUP=$(az group list \
  --query "[0].name" \
  -o tsv)

echo "Using Resource Group: $RESOURCE_GROUP"

if [ -z "$RESOURCE_GROUP" ]; then
  echo "No resource group found!"
  exit 1
fi

# =========================
# STEP 2: Create Storage Account
# =========================
echo "Creating Storage Account: $STORAGE_ACCOUNT_NAME"

az storage account create \
  --name $STORAGE_ACCOUNT_NAME \
  --resource-group $RESOURCE_GROUP \
  --location $LOCATION \
  --sku Standard_LRS \
  --kind StorageV2

# =========================
# STEP 3: Get Storage Account Key
# =========================
ACCOUNT_KEY=$(az storage account keys list \
  --resource-group $RESOURCE_GROUP \
  --account-name $STORAGE_ACCOUNT_NAME \
  --query "[0].value" \
  -o tsv)

# =========================
# STEP 4: Create Blob Container
# =========================
echo "Creating Blob container: $CONTAINER_NAME"

az storage container create \
  --name $CONTAINER_NAME \
  --account-name $STORAGE_ACCOUNT_NAME \
  --account-key $ACCOUNT_KEY \
  --public-access off

# =========================
# DONE
# =========================
echo "Setup Completed Successfully!"
echo "Storage Account: $STORAGE_ACCOUNT_NAME"
echo "Container: $CONTAINER_NAME"
echo "Resource Group: $RESOURCE_GROUP"