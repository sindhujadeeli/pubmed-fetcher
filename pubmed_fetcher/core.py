from typing import List, Dict
from Bio import Entrez
import csv

Entrez.email = "your_email@example.com"  # Replace with your real email

PHARMA_KEYWORDS = [
    'pharma', 'biotech', 'therapeutics', 'inc', 'corp', 'laboratories',
    'genentech', 'novartis', 'pfizer', 'roche', 'gsk', 'ltd', 'llc', 'solutions'
]

ACADEMIC_KEYWORDS = [
    'university', 'college', 'institute', 'school', 'hospital', 'department'
]

def is_pharma_or_biotech_affiliation(affiliation: str) -> bool:
    affil = affiliation.lower()
    return (
        any(k in affil for k in PHARMA_KEYWORDS)
        and not any(a in affil for a in ACADEMIC_KEYWORDS)
    )

def fetch_pubmed_ids(query: str, max_results: int = 100) -> List[str]:
    with Entrez.esearch(db="pubmed", term=query, retmax=max_results) as handle:
        record = Entrez.read(handle)
    return record["IdList"]

def fetch_pubmed_details(ids: List[str]) -> List[Dict]:
    if not ids:
        return []
    with Entrez.efetch(db="pubmed", id=','.join(ids), retmode="xml") as handle:
        records = Entrez.read(handle)
    return records["PubmedArticle"]

def extract_relevant_info(articles: List[Dict], debug: bool = False) -> List[Dict[str, str]]:
    results = []

    for article in articles:
        try:
            medline = article.get("MedlineCitation", {})
            article_info = medline.get("Article", {})
            title = article_info.get("ArticleTitle", "")

            pub_date = article_info.get("Journal", {}).get("JournalIssue", {}).get("PubDate", {})
            pub_date_str = " ".join(str(pub_date.get(k, '')) for k in ["Year", "Month", "Day"] if pub_date.get(k))

            authors = article_info.get("AuthorList", [])
            article_ids = article.get("PubmedData", {}).get("ArticleIdList", [])
            paper_id = next((i for i in article_ids if i.startswith("1") or i.isdigit()), "")

            non_academic_authors = []
            affiliations = set()
            corresponding_email = ""

            for author in authors:
                name = f"{author.get('ForeName', '')} {author.get('LastName', '')}".strip()
                aff_infos = author.get("AffiliationInfo", [])

                for aff in aff_infos:
                    affil_text = aff.get("Affiliation", "")
                    if debug:
                        print(f"Author: {name}, Affiliation: {affil_text}")

                    if is_pharma_or_biotech_affiliation(affil_text):
                        non_academic_authors.append(name)
                        affiliations.add(affil_text)

                    if '@' in affil_text and not corresponding_email:
                        corresponding_email = affil_text.split()[-1]

            if non_academic_authors:
                results.append({
                    "PubmedID": paper_id,
                    "Title": title,
                    "Publication Date": pub_date_str,
                    "Non-academic Author(s)": "; ".join(non_academic_authors),
                    "Company Affiliation(s)": "; ".join(affiliations),
                    "Corresponding Author Email": corresponding_email
                })

        except Exception as e:
            if debug:
                print(f"Error processing article: {e}")

    return results

def search_and_filter_papers(query: str, debug: bool = False) -> List[Dict[str, str]]:
    ids = fetch_pubmed_ids(query)
    articles = fetch_pubmed_details(ids)
    return extract_relevant_info(articles, debug=debug)

def save_to_csv(papers: List[Dict[str, str]], filename: str) -> None:
    fieldnames = [
        "PubmedID", "Title", "Publication Date",
        "Non-academic Author(s)", "Company Affiliation(s)", "Corresponding Author Email"
    ]
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(papers)
