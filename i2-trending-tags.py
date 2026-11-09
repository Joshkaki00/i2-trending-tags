# Brute force, sorting every tag and count by pair, biggest first

def trending_tags(tags, k):
    counts = {}
    for t in tags:
        counts[t] = counts.get(t, 0) + 1

    # sort every (tag, count) pair by count, biggest first
    ranked = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)

    return [tag for tag, _ in ranked[:k]]