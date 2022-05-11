def breakingRecords(scores):
    minScore = maxScore = scores[0]
    minTimes = maxTimes = 0
    for i in range(1, len(scores)):
        if scores[i] < minScore:
            minScore = scores[i]
            minTimes += 1
        elif scores[i] > maxScore:
            maxScore = scores[i]
            maxTimes += 1

    return [maxTimes, minTimes]
