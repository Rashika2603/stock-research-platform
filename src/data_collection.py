"""
Data Collection Module

Author: Rashika Agarwal

Purpose:
Download and store historical stock market data for
technology companies used throughout the project.
"""

# Yahoo Finance library for downloading historical market data
import yfinance as yf

# Stocks used throughout the project:
# AAPL: Apple | MSFT: Microsoft | GOOGL: Alphabet Inc. (Google's parent company) | NVDA: Nvidia | TSLA: Tesla
tickers = ["AAPL", "MSFT", "GOOGL", "NVDA", "TSLA"]

for ticker in tickers:
    print(f"\nDownloading {ticker}...")

    df = yf.download(
        ticker,
        start="2020-01-01", # Capture post-COVID market behavior and recent trends
        auto_adjust=True,   # Adjust prices for stock splits and dividends
        progress=False      
    )

    # Remove the extra MultiIndex header created by yfinance
    if df.columns.nlevels > 1:
        df.columns = df.columns.droplevel(1)

    # Save clean CSV
    df.to_csv(f"data/raw/{ticker}.csv")

    print(f"{ticker} saved. Shape: {df.shape}")

print("\nAll files downloaded successfully!")