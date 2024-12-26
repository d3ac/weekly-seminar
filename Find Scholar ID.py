import requests

# search for the paper on https://arxiv.org/

arxiv_id = "2202.10324"

url = f"https://api.semanticscholar.org/v1/paper/arXiv:{arxiv_id}"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    semantic_scholar_id = data.get("paperId")
    print(f"![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F{semantic_scholar_id}%3Ffields%3DcitationCount)")
else:
    print(f"Error code : {response.status_code}")
