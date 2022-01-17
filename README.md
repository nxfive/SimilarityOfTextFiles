# SimilarityOfTextFiles

Hello everyone!

This project based only on functions check similarity of the two given texts.
Steps:
1. Split the text into sentences
2. Split the senstence into words 
3. Calculate how many words from one sentence are repeated in the other
4. Check nr. 3 for all sentences and save only the most similar value of the indicator.
5. Calculate the mean of the most similar value for every sentence.

*In the function named calc_words_repetition is 'break', because when we 
find the same word, we do not search the list of words any further, we write that the word appears in the second sentence. 
We do not count repetitions now. 
