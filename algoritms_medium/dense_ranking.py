import time
import random 



score = sorted(random.sample(range(1,10000), 1000), reverse=True)
alice = random.sample(range(1,10000), 1000)
 

#avg(0,04) sec

# def climbingLeaderboard(scores, alice):
#     rank = []
#     alice = sorted(alice)
#     scores = sorted(set(scores), reverse=True)
    
#     #max_alice < min_scores
#     if alice[-1] < scores[-1]:
#         return [len(scores) + 1] * len(alice)
#     for rank_alice in alice:
#         ind = 1 
#         if rank_alice < scores[-1]:
#             rank.append(len(scores) + 1)
#             continue
#         for elem in scores:                
#             if rank_alice >= elem:
#                 rank.append(ind)
#                 break
#             ind += 1

#     return rank

#avg(9) sec

# def climbingLeaderboard(scores, alice):
#     scores = sorted(set(scores))
#     last_rank = len(scores) + 1
#     mapper = {range(scores[0]): last_rank}
#     length = len(scores)
#     result = []
#     for idx in range(length - 1):
#         mapper[range(scores[idx], scores[idx + 1])] = last_rank - idx - 1

#     for score in alice:
#         for rang, rank in mapper.items():
#             if score > max(list(mapper.keys())[-1]):
#                 result.append(1)
#                 break
#             if score in rang:
#                 result.append(rank)
#     return result

#avg(0,0004) sec
def climbingLeaderboard(scores, alice):
    scores = sorted(list(set(scores)))
    idx = 0
    rank_list = []
    n = len(scores)
    for i in alice:
        while (n > idx and i >= scores[idx]):
            idx += 1
        rank_list.append(n + 1 - idx)
    return rank_list


start_time = time.time()
print(climbingLeaderboard(score, alice))
print("--- %s seconds ---" % (time.time() - start_time))
