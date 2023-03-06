import weibo_scraper

hotwords = weibo_scraper.get_realtime_hotwords()
for hw in hotwords:
    print(str(hw))