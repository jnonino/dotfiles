#!/usr/bin/env python3
"""
GitHub Organization Repository Cloner
Fetches all organizations for a user and clones all repositories from each organization.
"""

import os
import sys
import subprocess
import requests
from typing import List, Dict


def get_user_organizations(username: str) -> List[Dict]:
    """Fetch all organizations the user is a member of."""
    url = f"https://api.github.com/users/{username}/orgs"

    try:
        response = requests.get(url)
        response.raise_for_status()
        orgs = response.json()
        print(f"Found {len(orgs)} organizations for user '{username}'")
        return orgs
    except requests.exceptions.RequestException as e:
        print(f"Error fetching organizations: {e}")
        sys.exit(1)


def get_org_repositories(org_name: str) -> List[Dict]:
    """Fetch all repositories for an organization."""
    repos = []
    page = 1
    per_page = 100

    while True:
        url = f"https://api.github.com/orgs/{org_name}/repos"
        params = {"page": page, "per_page": per_page}

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            page_repos = response.json()

            if not page_repos:
                break

            repos.extend(page_repos)
            page += 1

        except requests.exceptions.RequestException as e:
            print(f"Error fetching repositories for {org_name}: {e}")
            break

    print(f"  Found {len(repos)} repositories in '{org_name}'")
    return repos


def clone_repository(https_url: str, target_dir: str, repo_name: str):
    """Clone a repository using HTTPS."""
    try:
        print(f"    Cloning {repo_name}...")
        subprocess.run(
            ["git", "clone", https_url],
            cwd=target_dir,
            check=True,
            capture_output=True,
            text=True
        )
        print(f"    ✓ Successfully cloned {repo_name}")
    except subprocess.CalledProcessError as e:
        print(f"    ✗ Failed to clone {repo_name}: {e.stderr}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <github_username>")
        sys.exit(1)

    username = sys.argv[1]
    print(f"Fetching organizations for GitHub user: {username}\n")

    # Get all organizations
    organizations = get_user_organizations(username)

    if not organizations:
        print("No organizations found.")
        return

    # Process each organization
    for org in organizations:
        org_name = org['login']
        print(f"\nProcessing organization: {org_name}")

        # Create organization directory
        org_dir = org_name
        if not os.path.exists(org_dir):
            os.makedirs(org_dir)
            print(f"  Created directory: {org_dir}")
        else:
            print(f"  Directory already exists: {org_dir}")

        # Get all repositories for this organization
        repositories = get_org_repositories(org_name)

        # Clone each repository
        for repo in repositories:
            repo_name = repo['name']
            https_url = repo['clone_url']

            # Check if repository already exists
            repo_path = os.path.join(org_dir, repo_name)
            if os.path.exists(repo_path):
                print(f"    ⊘ {repo_name} already exists, skipping...")
                continue

            clone_repository(https_url, org_dir, repo_name)

    print("\n✓ All done!")


if __name__ == "__main__":
    main()
