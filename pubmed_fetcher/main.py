import argparse
from pubmed_fetcher.core import search_and_filter_papers, save_to_csv

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with pharma/biotech authors.")
    parser.add_argument("query", type=str, help="Search query for PubMed")
    parser.add_argument("-f", "--file", type=str, help="Output CSV filename")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug output")

    args = parser.parse_args()

    papers = search_and_filter_papers(args.query, debug=args.debug)

    if not papers:
        print("No relevant papers found.")
    elif args.file:
        save_to_csv(papers, args.file)
    else:
        for paper in papers:
            print(paper)

if __name__ == "__main__":
    main()
