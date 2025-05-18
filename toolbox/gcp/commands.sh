# This script contains a series of commands to interact with Google Cloud services.

# view all the services enabled in the project
gcloud services list --project "project_id_here"

# create API key
gcloud services api-keys create --project "project_id_here" \
  --display-name "API Key for Google Cloud Services"



