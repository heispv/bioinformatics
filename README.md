# bioinformatics

To clone this repository using HTTPS run the code below in your terminal:
```
git clone https://github.com/heispv/bioinformatics.git
```

* You can retrieve all the functions within this [Python file](https://github.com/heispv/bioinformatics/blob/master/functions.py). :wink:
***
In this collection, you will find all the notebooks along with their file descriptions and publish dates. Each notebook contains examples that showcase the results of various functions. 🙂

| Notebook Name | Comment | Publish Date |
| ----- | ----- | ----- |
| [Counting Words](https://github.com/heispv/bioinformatics/blob/master/counting-words.ipynb) | To compute Count(Text, Pattern), our plan is to “slide a window” down Text, checking whether each k-mer substring of Text matches Pattern. We will therefore refer to the k-mer starting at position i of Text as Text(i, k) | 21 July 2023 |
| [Best Common Patterns](https://github.com/heispv/bioinformatics/blob/master/frequent-words-problem.ipynb) | To calculate the `best common patterns` in a given sequence (ori), we can begin by creating a function that generates a `frequency table` of patterns based on their k-mer values. Then, we proceed to develop another function that identifies and selects the most frequently occurring patterns based on the k-mer values. By following these steps, we can effectively extract the most prevalent patterns in the ori sequence. | 21 July 2023 |
| [Reverse Complement](https://github.com/heispv/bioinformatics/blob/master/reverse-complement.ipynb) | In DNA, each strand is read from 3' to 5'. Therefore, to generate a complementary strand, we need to create a function that first reverses the original strand and then generates the complementary sequence based on the reversed strand. | 22 July 2023 |
| [Pattern Index Finder V1](https://github.com/heispv/bioinformatics/blob/master/pattern-index.ipynb) - [Pattern Index Finder V2(For Real Data)](https://github.com/heispv/bioinformatics/blob/master/pattern-index-2.ipynb) | Here we created a function which returns a list of the staring index of a pattern in a sequence. | 22 July 2023 |
| [Clump Finding](https://github.com/heispv/bioinformatics/blob/master/clump-finding-real.ipynb) | We defined a k-mer as a "clump" if it appears many times within a short interval of the genome. More formally, given integers L and t, a k-mer Pattern forms an (L, t)-clump inside a (longer) string Genome if there is an interval of Genome of length L in which this k-mer appears at least t times, so we created a function called `find_clumps(seq, k, L, t)` which also uses the function `freq_table(seq, k)` underhood. | 22 July 2023 |
| [Clump Finding (for Real Data)](https://github.com/heispv/bioinformatics/blob/master/clump-finding.ipynb) | In this notebook, we have optimized the `find_clump(seq, k, L, t)` function to efficiently detect clumps in real-world examples. This enhancement was necessary as the previous implementation proved to be considerably slow for such scenarios. Additionally, we introduced a new function named `freq_index(seq, k)`, which also contributes to the improved performance by providing a list of starting indices for each pattern.   | 23 July 2023 |
| [Skew Diagram](https://github.com/heispv/bioinformatics/blob/master/skew-diagram.ipynb) | In this particular section, our primary objective is to create a function called `skew_diagram(seq)` to analyze the DNA sequence. Notably, we have observed that the frequency of the GC base pair increases in the forward half-strand from the origin (ori) to the termination (ter), while it decreases in the reverse half-strand. To accurately visualize these fluctuations, we will represent the nucleotides as follows: C will be replaced with -1, G with +1, and T and A with 0. This representation will allow us to illustrate the changing pattern of the GC frequency effectively. Furthermore, by utilizing the "skew_diagram" function, we will be able to generate a skew diagram and identify the location of the ori, which is characterized by the minimum value on the diagram. This will enable us to pinpoint the specific position where the DNA replication process begins. | 25 July 2023 |
| [Hamming Distance](https://github.com/heispv/bioinformatics/blob/master/hamming-distance.ipynb) | We say that position i in k-mers p1 … pk and q1 … qk is a mismatch if pi ≠ qi. For example, CGAAT and CGGAC have two mismatches. The number of mismatches between strings p and q is called the Hamming distance between these strings and is denoted `hamming_distance(p, q)`. | 26 July 2023 |
| [Approximate Pattern Matching Problem](https://github.com/heispv/bioinformatics/blob/master/approximate_pattern_matching_problem.ipynb) | We say that a k-mer Pattern appears as a substring of Text with at most d mismatches if there is some k-mer substring Pattern' of Text having d or fewer mismatches with Pattern, i.e., `hamming_distance(Pattern, Pattern') ≤ d`. Our observation that a DnaA box may appear with slight variations leads to the following generalization of the Pattern Matching Problem, and so we use the `approximate_pattern_matching(pattern, seq, d)` fucntion to address this problem. | 26 July 2023 |
| [Generating the Neighborhood of a String](https://github.com/heispv/bioinformatics/blob/master/neighborhood-of-a-string.ipynb) | In this notebook, we will define a function named `neighborhood(pattern, d)`. The function utilizes the pre-existing hamming distance calculation to generate a set of sequences that are within a specified maximum hamming distance, 'd', from the given 'pattern' | 28 July 2023 |
