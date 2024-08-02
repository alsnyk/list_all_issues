import requests
import os

SNYK_TOKEN = "<SNYK_TOKEN>"
ORG_ID = "<ORG_ID>"

BASE_URL = "https://api.snyk.io"

def get_issues_page(next_url):

    # Add "next url" on to the BASE URL
    url = BASE_URL + next_url

    headers = {
        'Accept': 'application/vnd.api+json',
        'Authorization': f'token {SNYK_TOKEN}'
    }

    return requests.request("GET", url, headers=headers)

def get_all_issues():
    next_url = f"/rest/orgs/{ORG_ID}/issues?version=2024-02-28&limit=100"

    all_issues = []

    while next_url is not None:
        res = get_issues_page(next_url).json()

        if 'links' in res and 'next' in res['links']:
            next_url = res['links']['next']
        else:
            next_url = None

        # add to list
        if 'data' in res:
            all_issues.extend(res['data'])

    return all_issues


def main():
    all_issues = get_all_issues()
    for issue in all_issues:

        # TODO: do something with issue here \/
        print(issue['id'], issue['attributes']['title'], sep='\t')

main()