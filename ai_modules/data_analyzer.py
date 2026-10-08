import pandas as pd

def analyze_campaign_performance(file_path):
    """
    Reads campaign data and returns actionable insights.
    """
    try:
        df = pd.read_csv(file_path)
        avg_ctr = df['CTR'].mean()
        return {"average_ctr": avg_ctr, "status": "Optimized"}
    except Exception as e:
        return {"error": str(e)}
