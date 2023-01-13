# Spam_Detection_Naive_bayes

We are given a dataset of user-generated reviews in the form of training dataset and testing dataset. We have created a 'Naive Bayes classifier', which classifies the reviews into fake or legitimate for 20 hotels in Chicago. The training dataset has labels which tell if the review is 'deceptive' or 'truthful' along with the review.

Bayesian Classifier:
To classify the reviews into 'deceptive' and 'truthful', we calculated the probability that a given review is 'truthful' conditioned that it has the words ('P('truthful'|words)'). Or else, it is 'deceptive'.

We first get the training data file('deceptive.train.txt') into the form of a dictionary called train_data which has the keys 'labels','objects' and 'classes'. The values for each of the keys is in the form of lists. The values for 'labels' is whether the particular review is 'truthful' or 'deceptive'. In the case of the value for 'objects', it is a list of all the reviews. And finally the value for 'classes' is a list of possible cases i.e 'truthful' or 'deceptive'.

We then use string and translate function to preprocess the review sentences (training points) in which we remove the punctuation marks and strip the sentences of any blankspaces at start or end of the line and also lowercase all words in the review

We then store the counts of reviews labeled truthful and deceptive accordingly and also the count of total words in both the classes and then use dictionaries to store the frequency of occurrence for each word from the reviews in both the classes

We use these for above calculated values for calculating the probability of the given word, conditioned that the review is 'truthful' or 'deceptive'.((P(word|'truthful') or P(word|'deceptive'))

The probability of review that contains words (word1 , word2 …) to be ‘truthful’ is proportional to the probability to get the ‘truthful’ , multiplied by a product of probabilities of the words belonging to the ‘truthful’ class.

To calculate the word given ‘truthful’ probability , we divide the sum of frequency count of the word in truthful category and a constant with sum of total number of words in the same category and constant into total number of unique words from both the categories

We ran a for loop for all the words of each of the review in the test data set. We get the probability that is already calculated for each word and multiply it to the corresponding truthful probability or deceptive probability.((P('truthful') * P(word1|truthful) * P(word2|truthful)...) and (P('deceptive') * P(word1|deceptive) P(word2|deceptive)...))

We executed the above calculation first using basic math but for some words ,the word given truthful (or deceptive) probability was going to a very low value and even though the probability wasn’t exactly zero (thus ‘if’ condition did not help) the final probability after multiplication resulted in zero for reviews . Hence used log calculation to get the final probabilities

We store each of the above calculated probability into variables called p_true and p_false . Compare them and then we store the result as 'truthful' otherwise it is 'deceptive'.

Result:

The Result is stored in the form of a list which contains if the given review from the test data set is 'truthful' or 'deceptive'. We are getting a accuracy of 85%.
