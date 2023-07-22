# bioinformatics

To clone this repository using HTTPS run the code below in your terminal:
```
git clone https://github.com/heispv/bioinformatics.git
```


| Notebook Name | Comment | Publish Date |
| ----- | ----- | ----- |
| [Counting Words](https://github.com/heispv/bioinformatics/blob/master/counting-words.ipynb) | To compute Count(Text, Pattern), our plan is to “slide a window” down Text, checking whether each k-mer substring of Text matches Pattern. We will therefore refer to the k-mer starting at position i of Text as Text(i, k) | 21 July 2023 |
| [What are the Best Common Patterns](https://github.com/heispv/bioinformatics/blob/master/frequent-words-problem.ipynb) | To calculate the `best common patterns` in a given sequence (ori), we can begin by creating a function that generates a `frequency table` of patterns based on their k-mer values. Then, we proceed to develop another function that identifies and selects the most frequently occurring patterns based on the k-mer values. By following these steps, we can effectively extract the most prevalent patterns in the ori sequence. | 21 July 2023 |
| [Reverse Complement](https://github.com/heispv/bioinformatics/blob/master/reverse-complement.ipynb) | In DNA, each strand is read from 3' to 5'. Therefore, to generate a complementary strand, we need to create a function that first reverses the original strand and then generates the complementary sequence based on the reversed strand. | 22 July 2023 |
| [Pattern Index Finder V1](https://github.com/heispv/bioinformatics/blob/master/pattern-index.ipynb) - [Pattern Index Finder V2(For Real Data)](https://github.com/heispv/bioinformatics/blob/master/pattern-index-2.ipynb) | Here we created a function which returns a list of the staring index of a pattern in a sequence. | 22 July 2023 |
