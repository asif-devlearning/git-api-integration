GitHub Collaboration Management Script

This repository contains a Python script for managing collaboration on GitHub repositories. The script allows users to fetch collaborators from a specified repository, convert the retrieved data into a CSV file, and further convert it into an Excel file for easier visualization. Additionally, it facilitates the addition of new collaborators to the repository with specified permissions.

Features:
Fetch Collaborators: Fetches collaborators from a GitHub repository using the GitHub API and saves their information to a CSV file.
Convert to Excel: Converts the CSV file containing collaborator information into an Excel file for better organization and readability.
Add Collaborator: Adds new collaborators to the repository with specified permissions, facilitating efficient collaboration management.
How to Use:
Setup:

Ensure you have Python installed on your system.
Clone this repository to your local machine.
Authentication:

Obtain a GitHub token with appropriate permissions.
Provide your GitHub username and the obtained token when prompted by the script.
Repository Details:

Enter the organization name and repository name for which you want to manage collaboration.
Executing the Script:

Run the main.py script.
Follow the prompts to fetch collaborators, convert the data to Excel, and add new collaborators as needed.
Requirements:
Python 3.x
requests library
csv module
os module
pandas library
Usage Notes:
Ensure that your GitHub token has sufficient permissions to fetch collaborators and add new collaborators to the repository.
The script provides interactive prompts for ease of use and requires user input for GitHub authentication and repository details.
Contributors:
Mohammed67-lab
Feel free to contribute to this project by opening issues or submitting pull requests. Your contributions are highly appreciated!

Disclaimer: This script interacts with GitHub's API and modifies repository data. Use it responsibly and ensure that you have the necessary permissions before executing any actions.