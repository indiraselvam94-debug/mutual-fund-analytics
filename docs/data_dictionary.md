\# Mutual Fund Analytics - Data Dictionary



\## Dataset: nav\_history\_clean.csv



| Column Name     | Data Type | Description             |

| --------------- | --------- | ----------------------- |

| scheme\_code     | INTEGER   | Unique AMFI scheme code |

| scheme\_name     | TEXT      | Mutual fund scheme name |

| fund\_house      | TEXT      | AMC/Fund House name     |

| scheme\_type     | TEXT      | Type of scheme          |

| scheme\_category | TEXT      | Category of mutual fund |

| date            | DATE      | NAV date                |

| nav             | REAL      | Net Asset Value         |



\## Source



\* mfapi.in

\* AMFI India



\## Cleaned Rules Applied



1\. Converted date column to datetime.

2\. Sorted data by scheme code and date.

3\. Removed duplicate records.

4\. Converted NAV to numeric values.

5\. Removed invalid NAV values (<= 0).

6\. Saved cleaned dataset into data/processed.


