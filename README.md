# Open Source Project Health Analytics

## Overview

This project analyzes the health and popularity of open-source Python repositories using data collected from the GitHub API.

The goal is to explore how repository popularity relates to community engagement and maintenance activity through data collection, data cleaning, exploratory data analysis, SQL, Python, and Power BI.

## Business Questions

- How do stars and forks differ across repository popularity groups?
- Which popularity group has the highest average fork-to-star ratio?
- How many open issues do repositories have on average?
- How recently have the analyzed repositories been updated?
- What can these metrics tell us about open-source project activity?

## Tools and Technologies

- **Python:** Data collection, validation, transformation, and analysis
- **GitHub REST API:** Repository data collection
- **SQL:** Data analysis and querying
- **Power BI:** Interactive dashboard and data visualization
- **Git and GitHub:** Version control and project documentation

## Dataset

The dataset contains **233 unique Python repositories** collected from GitHub and divided into three star-based popularity groups.

| Popularity Group | Repository Count |
|---|---:|
| High Popularity | 33 |
| Medium Popularity | 100 |
| Lower Popularity | 100 |
| **Total** | **233** |

The dataset includes repository names, programming language, stars, forks, open issues, fork-to-star ratio, last update timestamp, and days since the last update.

**Sampling note:** The medium- and lower-popularity groups are limited samples returned by GitHub Search API queries. The dataset is not a random or fully representative sample of all Python repositories.

## Methodology

1. Collect repository metadata from GitHub using Python.
2. Divide repositories into star-based popularity groups.
3. Validate records, check missing values and duplicates, and verify group assignments.
4. Prepare a clean dataset for analysis and Power BI.
5. Calculate repository engagement and update-recency metrics.
6. Build an interactive Power BI dashboard to compare the groups.

## Key Findings

- The high-popularity group has the highest average stars and forks. This is expected because popularity groups were defined using star counts.
- The medium-popularity sample has the highest average fork-to-star ratio among the three groups.
- The groups differ in average open issues, but open issues alone do not indicate poor project health.
- Update recency provides a snapshot of recent maintenance activity, not a complete measure of long-term project sustainability.

These findings are descriptive and should not be interpreted as evidence that popularity causes stronger engagement or better maintenance.
## SQL Analysis Outputs

The project uses SQLite to analyze repository metadata stored in the `repositories_powerbi` table.

Five SQL reports are generated in `data/processed/sql_results/`:

| Report | Description |
|---|---|
| `01_repository_counts.csv` | Repository counts by popularity group |
| `02_group_metrics.csv` | Average stars, forks, and open issues by group |
| `03_fork_to_star_ratio.csv` | Average fork-to-star ratio by group |
| `04_update_recency.csv` | Average days since the last update by group |
| `05_top_open_issues.csv` | Top 10 repositories by open issue count |

### Analytical Summary

- The dataset contains 233 repositories: 33 high-popularity, 100 medium-popularity, and 100 lower-popularity repositories.
- The high-popularity sample has the highest average stars and forks, consistent with the star-based grouping method.
- The medium-popularity sample has the highest average fork-to-star ratio in the current dataset.
- Open issue counts and update recency should be interpreted alongside other project activity metrics rather than as standalone measures of project health.

The analysis is descriptive and reflects the collected dataset at a specific point in time.

## Power BI Dashboard

The dashboard includes:

- Total repositories
- Total stars
- Total forks
- Average fork-to-star ratio
- Average open issues
- Average stars by popularity group
- Average fork-to-star ratio by popularity group
- Average days since last update by popularity group
- A popularity-group slicer for interactive filtering

The Power BI report is available in `powerbi/Open_Source_Project_Health_Analytics.pbix`.

## Project Structure

```text
Open-Source-Project-Health-Analytics/
├── data/
│   ├── raw/
│   └── processed/
├── src/
├── sql/
├── powerbi/
├── docs/
├── README.md
├── requirements.txt
└── .gitignore
```

Raw data files may be excluded from version control. Run the data collection and preparation scripts to reproduce the dataset.

## Limitations

- GitHub Search API results are subject to query and result limits.
- The dataset represents a snapshot in time.
- Star counts, forks, open issues, and update recency are proxies for activity, not definitive measures of project health.
- The results may not generalize to every programming language or open-source community.

## Future Improvements

- Expand data collection across additional programming languages.
- Collect repository history at regular intervals to analyze trends over time.
- Add contributor activity, issue resolution time, pull request metrics, and release frequency.
- Develop SQL queries for repeatable analytical reporting.
- Improve the dashboard with additional filters and drill-through analysis.

## Author

Created as a personal Data Analytics portfolio project.
