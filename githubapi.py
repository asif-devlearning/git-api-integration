import requests
import csv
import os
import pandas as pd

def fetch_collaborators(api_url, repo_owner, repo_name, username, token):
    """Fetches collaborators from the GitHub API and saves them to a CSV file."""
    # Construct URL to list collaborators for the repository
    list_collaborators = f"{api_url}repos/{repo_owner}/{repo_name}/collaborators"

    # Send GET request to GitHub API to fetch collaborators
    git_response = requests.get(list_collaborators, auth=(username, token))

    # Name for the CSV file
    create_csv = "list_of_collab.csv"

    # Check if the CSV file already exists and remove it if it does
    if os.path.exists(create_csv):
        os.remove(create_csv)
        print("----- Existing CSV removed, will create a new one -----")

    # Define CSV fields
    fields = ['Collaborator_id', 'Collaborator_Name', 'role_name', 'pull_permission', 'push_permissions']

    if git_response.status_code == 200:
        # Initialize outer list to hold collaborator data
        outer_list = []

        # Loop through each collaborator and extract relevant information
        for collaborator in git_response.json():
            # Create an inner list with collaborator data
            inner_list = [collaborator['id'], collaborator['login'], collaborator['role_name'], collaborator['permissions']['pull'], collaborator['permissions']['push']]
            # Append inner list to outer list
            outer_list.append(inner_list)

        # Write data to CSV file
        with open(create_csv, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fields)
            csvwriter.writerows(outer_list)
    else:
        print("Resource not found")

    return create_csv

def convert_to_excel(csv_file, excel_file):
    """Converts the CSV file to an Excel file."""
    # Read the CSV file into a DataFrame
    list_members_df = pd.read_csv(csv_file)

    # Write the DataFrame to an Excel file
    list_members_df.to_excel(excel_file, index=False)
    print("List successfully completed in an excel file")

def add_collaborator(api_url, repo_owner, repo_name, username, token):
    """Adds a collaborator to the repository."""
    add_member_username = input("Please enter the GitHub username of the user you would like to add: ")
    if add_member_username:
        # Construct URL for adding a collaborator
        add_member_api_url = f"{api_url}repos/{repo_owner}/{repo_name}/collaborators/{add_member_username}"

        # JSON payload for specifying permissions
        payload = {"permission": "push"}

        # Send PUT request to add the collaborator
        headers = {"Authorization": f"Bearer {token}"}
        add_member_response = requests.put(add_member_api_url, json=payload, headers=headers)
        print(add_member_response.status_code)

        if add_member_response.status_code == 201:
            print("Member add request successfully sent")
        else:
            print("Failed to add member")
    else:
        print("No username provided")

def main():
    # GitHub API URL and authentication credentials
    api_url = "https://api.github.com/"
    username = "Mohammed67-lab"
    token = input("Please paste the GitHub token: ")

    # Input organization name and repository name
    repo_owner = input("Please write the organization name:")
    repo_name = input("Please input your repository name:")

    # Fetch collaborators and save to CSV
    csv_file = fetch_collaborators(api_url, repo_owner, repo_name, username, token)

    # Convert CSV to Excel
    excel_file = 'git_org_members.xlsx'
    convert_to_excel(csv_file, excel_file)

    # Add collaborator
    add_collaborator(api_url, repo_owner, repo_name, username, token)

if __name__ == "__main__":
    main()
