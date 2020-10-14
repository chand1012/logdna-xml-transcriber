from feed import generate_feed
from dna import get_logs

logs = get_logs()
feed = generate_feed(logs)
print(feed)