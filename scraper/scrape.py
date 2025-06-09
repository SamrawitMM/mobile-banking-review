from google_play_scraper import reviews, Sort
import pandas as pd

bank_apps = {
        "CBE": "com.combanketh.mobilebanking",
        "BoA": "com.boa.boaMobileBanking",
        "Dashen": "com.dashen.dashensuperapp"
}

all_reviews = []

for bank, app_id in bank_apps.items():
    result, _ = reviews(
        app_id,
        lang="en",
        country="us",
        sort=Sort.NEWEST,
        count=400
    )
    for r in result:
        all_reviews.append({
            "review": r['content'],
            "rating": r['score'],
            "date": r['at'].strftime('%Y-%m-%d'),
            "bank": bank,
            "source": "Google Play"
        })

df = pd.DataFrame(all_reviews)
df.to_csv("raw_reviews.csv", index=False)
