import numpy as np
import matplotlib.pyplot as plt

#=============================================================================
def freq_table(text, k):
  freq_table = {}
  n = len(text)

  for i in range(n - k + 1):
    pattern = text[i : i+k]

    if pattern not in freq_table.keys():
      freq_table[pattern] = 1
    else:
      freq_table[pattern] += 1

  return freq_table
#=============================================================================
def index_table(seq, k):
    index_table = {}

    for i in range(0, len(seq)-k+1):
        if (pattern := seq[i: i+k]) not in index_table:
            index_table[pattern] = [i]
        else:
            index_table[pattern].append(i)
    return index_table
#=============================================================================
def find_clumps(seq, k, L, t):
    idx_table = index_table(seq, k)
    clumps_num = 0
    clump_list = []

    for key in idx_table:
      for i in range(0, len(value := idx_table[key])):
        if (i+t-1 < len(value)) and (value[i+t-1] - value[i]) <= L-k:
          clumps_num += 1
          clump_list.append(key)
          break

    return clumps_num, clump_list
#=============================================================================
def reverse_complement(text):
  text = text.replace('A', 'a')
  text = text.replace('C', 'c')
  text = text.replace('T', 'A')
  text = text.replace('G', 'C')
  text = text.replace('a', 'T')
  text = text.replace('c', 'G')

  return text[::-1]
#=============================================================================
def best_patterns(text, k):
  best_patterns = []
  table = freq_table(text, k)
  max = np.max(list(table.values()))

  for key, value in table.items():
    if value == max:
      best_patterns.append(key)

  return best_patterns
#=============================================================================
def pattern_index(sequence, pattern):
  pattern_idx = []
  n = len(sequence)
  k = len(pattern)

  for i in range(n - k + 1):
    seq2check = sequence[i : i+k]
    if seq2check == pattern:
      pattern_idx.append(i)


  return pattern_idx
#=============================================================================
def skew_min_idx(skew_list):
    if not skew_list:
        return []

    min_value = min(skew_list)
    min_indices = [index for index, value in enumerate(skew_list) if value == min_value]
    return min_indices
#=============================================================================
def skew_diagram(seq):
    char_to_num_mapping = {'A': 0, 'T': 0, 'C': -1, 'G': 1}
    the_list = [char_to_num_mapping.get(char, None) for char in seq]

    skew_list = [0]
    cumsum = 0
    for num in the_list:
      if num != None:
        cumsum += num
        skew_list.append(cumsum)

    min_idx = skew_min_idx(skew_list)

    plt.figure(figsize=(6, 3))
    plt.plot(skew_list)
    plt.show()

    return skew_list, min_idx
#=============================================================================
def hamming_distance(p, q):

    distance = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            distance += 1

    return distance
#=============================================================================
def immidiate_neighbors(pattern):
    neighbors = set()

    for i in range(len(pattern)):
        for j in 'ATCG':
            if pattern[i] != j:
                to_add = pattern[:i] + j + pattern[i+1:]
                neighbors.add(to_add)

    return neighbors
#=============================================================================
def neighborhood(pattern, d):
    if d == 0:
        return pattern
    if len(pattern) == 1:
        return {'A', 'T', 'C', 'G'}

    neighbors = set()

    suffix_pattern = pattern[1:]
    suffix_neighbors = neighborhood(suffix_pattern, d)

    for suffix_neighbor in suffix_neighbors:
        if hamming_distance(suffix_pattern, suffix_neighbor) < d:
            for x in 'ATCG':
                neighbors.add(x + suffix_neighbor)
        else:
            neighbors.add(pattern[0] + suffix_neighbor)

    return neighbors