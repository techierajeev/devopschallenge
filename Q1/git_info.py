#!/bin/python
import sys
import  pandas as pd
import requests
import json
output_list = []

def get_repo_info(repo):
	commit_api = "https://api.github.com/repos/"+repo+"/commits"
	url_api = "https://api.github.com/repos/"+repo
	commit_resp =  requests.get(commit_api)
	url_resp = requests.get(url_api)
	clone_url =  url_resp.json().get('clone_url').encode('utf-8').strip();
	repo_name = url_resp.json().get('full_name').encode('utf-8').strip();
	latest_commit = commit_resp.json()[0]['sha'].encode('utf-8').strip();
	author =   json.loads(commit_resp.text)[0]['commit'].get('author').get('name').encode('utf-8').strip();	
	repo_info = [clone_url,repo_name,latest_commit,author];
	output_list.append(repo_info);

input = sys.argv[1]
with open(input) as content: 
	repo_list = [x.rstrip() for x in content]

for item in repo_list:
	get_repo_info(item); 

df  =  pd.DataFrame(output_list);
df.to_csv("Git_Info.csv",index=False,header=["CloneUrl","RepoName","LatestCommit","Author"]);
