import requests
import pandas as pd

# GitHub repository details
base_url = "https://api.github.com/repos/PatrickJS/awesome-cursorrules"
rules_path = "rules"  # Path to the "rules" folder

# Replace with your Personal Access Token
headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": "token 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"  # Add your PAT here
}

# Function to fetch directory contents from the GitHub API
def fetch_directory_contents(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch {url}. Status Code: {response.status_code}")
        return []

# Function to fetch raw file content
def fetch_raw_file_content(repo, file_path):
    raw_url = f"https://raw.githubusercontent.com/{repo}/main/{file_path}"
    response = requests.get(raw_url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch raw file content from {raw_url}. Status Code: {response.status_code}")
        return ""

# Step 1: Get the list of folders in the "rules" directory
rules_url = f"{base_url}/contents/{rules_path}"
folders = fetch_directory_contents(rules_url)

# Step 2: Loop through each folder and fetch ".cursorrules" content
repo_name = "PatrickJS/awesome-cursorrules"
data = []
for folder in folders:
    if folder['type'] == 'dir':  # Ensure it's a folder
        folder_name = folder['name']
        cursorrules_path = f"{rules_path}/{folder_name}/.cursorrules"
        content = fetch_raw_file_content(repo_name, cursorrules_path)
        
        if content:
            # Append folder name and file content
            data.append({'Folder Name': folder_name, 'Cursorrules Content': content})
        else:
            print(f"No .cursorrules file found in folder: {folder_name}")

# Step 3: Save the data to a CSV
df = pd.DataFrame(data)
df.to_csv("cursorrules_content.csv", index=False)

print("Scraping completed! Data saved to 'cursorrules_content.csv'.")