# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3721/
from sys import stdin
from heapq import heapify, heappush, heappop

l = [int(x) for x in stdin.readline().split(',')]
bricks = int(stdin.readline())
ladders = int(stdin.readline())

def calculate_max_building(l, bricks, ladders):
  heap = []
  heapify(heap)
  max_building_reached = 0
  for i in range(len(l)-1):
    diff = l[i+1] - l[i]
    if diff > 0:
      if ladders > 0:
        ladders -= 1
        heappush(heap, diff)
      elif len(heap) > 0 and diff > heap[0] and bricks >= heap[0]:
        bricks -= heap[0]
        heappop(heap)
        heappush(heap, diff)
      elif bricks >= diff:
        bricks -= diff
      else:
        return max_building_reached
    max_building_reached += 1
  return max_building_reached 

print(calculate_max_building(l, bricks, ladders))