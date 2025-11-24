---
slug: github-data-link-note-technical-overview
id: github-data-link-note-technical-overview
title: data-link
repo: justin-napolitano/data-link
githubUrl: https://github.com/justin-napolitano/data-link
generatedAt: '2025-11-24T18:34:55.225Z'
source: github-auto
summary: >-
  This repo lets you fetch data from the Nasdaq Data Link API using Python and
  Jupyter Notebooks. It's built for simplicity and modularity, separating
  concerns like initialization and data retrieval.
tags: []
seoPrimaryKeyword: ''
seoSecondaryKeywords: []
seoOptimized: false
topicFamily: null
topicFamilyConfidence: null
kind: note
entryLayout: note
showInProjects: false
showInNotes: true
showInWriting: false
showInLogs: false
---

This repo lets you fetch data from the Nasdaq Data Link API using Python and Jupyter Notebooks. It's built for simplicity and modularity, separating concerns like initialization and data retrieval.

## Key Components

- **Python 3.9+:** Ensure you're using this or a newer version.
- **Dependencies:** Run this to install the necessary package:
  
  ```bash
  pip install nasdaqdatalink
  ```

- **Jupyter Notebooks:** Explore datasets with notebooks like `Capital-Markets.ipynb` and `FreightRailEasyRead.ipynb`.

## Quick Start

1. Get your API key from Nasdaq and save it as `.key` in the root directory.
2. To fetch data for a sample ticker, run:

   ```bash
   python main.py
   ```

## Gotchas

Make sure your API key is correctly saved in the project root; otherwise, you'll run into issues. Future enhancements will include better error handling and possibly a CLI for flexible queries. 

Check it out: [data-link on GitHub](https://github.com/justin-napolitano/data-link).
