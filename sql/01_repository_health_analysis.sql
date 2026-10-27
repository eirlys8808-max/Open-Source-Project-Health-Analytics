-- Project: Open Source Project Health Analytics
-- Analysis: Repository health and popularity comparison
-- Dataset: 233 Python repositories collected from GitHub

-- Query 1: Count repositories by popularity group
SELECT
    star_group_label,
    COUNT(*) AS repository_count
FROM repositories_powerbi
GROUP BY star_group_label
ORDER BY
    CASE star_group_label
        WHEN 'High Popularity' THEN 1
        WHEN 'Medium Popularity' THEN 2
        WHEN 'Lower Popularity' THEN 3
        ELSE 4
    END;


-- Query 2: Compare stars, forks, and open issues
SELECT
    star_group_label,
    COUNT(*) AS repository_count,
    ROUND(AVG(stars), 2) AS average_stars,
    ROUND(AVG(forks), 2) AS average_forks,
    ROUND(AVG(open_issues), 2) AS average_open_issues
FROM repositories_powerbi
GROUP BY star_group_label
ORDER BY average_stars DESC;


-- Query 3: Compare fork-to-star ratios
SELECT
    star_group_label,
    ROUND(AVG(fork_to_star_ratio), 2)
        AS average_fork_to_star_ratio_pct,
    ROUND(MIN(fork_to_star_ratio), 2)
        AS minimum_ratio_pct,
    ROUND(MAX(fork_to_star_ratio), 2)
        AS maximum_ratio_pct
FROM repositories_powerbi
GROUP BY star_group_label
ORDER BY average_fork_to_star_ratio_pct DESC;


-- Query 4: Analyze repository update recency
SELECT
    star_group_label,
    ROUND(AVG(days_since_update), 2)
        AS average_days_since_update,
    MIN(days_since_update) AS minimum_days_since_update,
    MAX(days_since_update) AS maximum_days_since_update
FROM repositories_powerbi
GROUP BY star_group_label
ORDER BY average_days_since_update ASC;


-- Query 5: Identify repositories with the most open issues
SELECT
    name,
    stars,
    forks,
    open_issues,
    star_group_label
FROM repositories_powerbi
ORDER BY open_issues DESC
LIMIT 10;