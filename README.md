

#### 📄 PubMed Fetcher

#### 

A command-line Python program that fetches research papers from PubMed based on a user-provided query, filters for non-academic (e.g. pharma/biotech) author affiliations, and exports the results to a CSV file.

#### &nbsp;✅ Features



\- 🔎 Accepts any valid PubMed query

\- 🏢 Identifies and filters papers with non-academic author affiliations

\- 📄 Outputs a CSV file with:

&nbsp; - PubMed ID

&nbsp; - Title

&nbsp; - Publication Date

&nbsp; - Non-academic Author(s)

&nbsp; - Company Affiliation(s)

&nbsp; - Corresponding Author Email

\- ⚙️ CLI Options: `--help`, `--debug`, `--file`

\- 🧪 Fully typed Python code for readability and safety

#### 

#### &nbsp;🚀 Installation

##### 1\. Clone this Repository

git clone https://github.com/<your-username>/pubmed-fetcher.git

cd pubmed-fetcher



##### 2\. Install with Poetry

&nbsp;    poetry install

##### 🧑‍💻 Usage

Run the program using the get-papers-list command:

&nbsp;  poetry run get-papers-list "cancer therapy"



##### 🏗️ Code Structure



pubmed-fetcher/

├── pubmed\_fetcher/

│   ├── \_\_init\_\_.py

│   ├── core.py         # Core logic (fetching, filtering)

│   └── main.py         # CLI interface

├── pyproject.toml      # Poetry project file

├── poetry.lock

└── README.md



##### 📦 Dependencies

* Poetry
* Biopython — for Entrez API access
* typer — for CLI
* tqdm — for progress bars



&nbsp; Install them with:

&nbsp;        poetry install



##### 🔍 Heuristics Used

* Filters authors by checking affiliation strings for:
* Pharmaceutical, Biotech, or Healthcare company keywords
* Non-academic patterns (excluding "university", "institute", "college", etc.)



##### 📤 Publishing

* This project is ready to be:
* Split into module + CLI
* Published on TestPyPI (optional for bonus points)



###### 💡 Example



Run:

&nbsp; poetry run get-papers-list "cancer therapy" --file cancer\_output.csv



Example output in cancer\_output.csv:



PubMed ID	Title	Non-Academic Authors	Affiliation

12345678	Novel Cancer Treatment XYZ	Jane Doe, John Smith	Pfizer, Roche



##### 🧠 Tools Used

This project was built using:



* Python + Poetry
* PubMed API (via Biopython)
* LLM (ChatGPT) for guidance and code suggestions



##### 📜 License

&nbsp;   This project is open-source and free to use.













