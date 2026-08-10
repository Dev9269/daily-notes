from datetime import datetime, timezone, timedelta

def utc_now():
    return datetime.now(timezone.utc).isoformat()

def days_ago(days):
    return (datetime.now(timezone.utc) - timedelta(days=days)).isoformat()
