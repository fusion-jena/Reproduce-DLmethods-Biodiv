from bs4 import BeautifulSoup
import requests, lxml, os, json
import numpy

data = []
for x in range(0, 510, 10):
    params = {
        "q": 'biodivers* OR "genetic diversity" OR "*omic diversity" OR "phylogenetic diversity" OR "population diversity" OR "species diversity" OR "ecosystem diversity" OR "functional diversity" OR "microbial diversity" OR "soil diversity" AND "Deep Learning"',
        "hl": "en",
        "as_ylo": 2015,
        "as_yhi": 2021,
        "start": "{}".format(x),
    }
    headers = {
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
    }
    html = requests.get(
        "https://scholar.google.com/scholar", headers=headers, params=params, timeout=30
    ).text
    soup = BeautifulSoup(html, "lxml")
    for result in soup.select(".gs_ri"):
        try:
            title = result.select_one(".gs_rt").text
            title_link = result.select_one(".gs_rt a")["href"]
            publication_info = result.select_one(".gs_a").text
            snippet = result.select_one(".gs_rs").text
            cited_by = result.select_one("#gs_res_ccl_mid .gs_nph+ a")["href"]
            related_articles = result.select_one("a:nth-child(4)")["href"]
            try:
                all_article_versions = result.select_one("a~ a+ .gs_nph")["href"]
            except:
                all_article_versions = None

            data.append(
                {
                    "title": title,
                    "title_link": title_link,
                    "publication_info": publication_info,
                    "snippet": snippet,
                    "cited_by": f"https://scholar.google.com{cited_by}",
                    "related_articles": f"https://scholar.google.com{related_articles}",
                    "all_article_versions": f"https://scholar.google.com{all_article_versions}",
                }
            )
        except:
            pass
with open("Google_scholar_500_publications_run1.json", "w") as outfile:
    json.dump(data, outfile)
