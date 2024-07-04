-- Index

CREATE INDEX idx_stock_data_company_date ON stock_data (Company, Date);


-- Company Wise Daily Variation of Prices

SELECT 
    Company, 
    Date, 
    Open, 
    Close, 
    (Close - Open) AS DailyVariation
FROM stock_data
ORDER BY Company, Date;

-- Company Wise Daily Volume Change

SELECT 
    Company, 
    Date, 
    Volume, 
    LAG(Volume, 1) OVER (PARTITION BY Company ORDER BY Date) AS PreviousVolume,
    (Volume - LAG(Volume, 1) OVER (PARTITION BY Company ORDER BY Date)) AS DailyVolumeChange
FROM stock_data
ORDER BY Company, Date;

-- Median Daily Variation

SELECT 
    Company,
    ROUND(AVG(DailyVariation), 2) AS MedianDailyVariation
FROM (
    SELECT 
        Company,
        (Close - Open) AS DailyVariation
    FROM stock_data
)
GROUP BY Company;