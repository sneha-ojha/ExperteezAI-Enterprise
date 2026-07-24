import arxiv
import time

print("Creating client...")
client = arxiv.Client()

print("Creating search...")
search = arxiv.Search(
    query="GPU",
    max_results=2
)

print("Starting timer...")
start = time.time()

try:
    for i, paper in enumerate(client.results(search), start=1):
        print(f"\nPaper {i}")
        print("Title:", paper.title)
        print("URL:", paper.entry_id)

    print("\nFinished successfully.")

except Exception as e:
    print("ERROR:", e)

print("Time:", time.time() - start)