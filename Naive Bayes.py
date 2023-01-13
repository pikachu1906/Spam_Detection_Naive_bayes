# SeekTruth.py : Classify text objects into two categories
#
# PLEASE PUT YOUR NAMES AND USER IDs HERE
#
# Based on skeleton code by D. Crandall, October 2021
#

import sys
import math
def load_file(filename):
    objects=[]
    labels=[]
    with open(filename, "r") as f:
        for line in f:
            parsed = line.strip().split(' ',1)
            labels.append(parsed[0] if len(parsed)>0 else "")
            objects.append(parsed[1] if len(parsed)>1 else "")

    return {"objects": objects, "labels": labels, "classes": list(set(labels))}

# classifier : Train and apply a bayes net classifier
#
# This function should take a train_data dictionary that has three entries:
#        train_data["objects"] is a list of strings corresponding to reviews
#        train_data["labels"] is a list of strings corresponding to ground truth labels for each review
#        train_data["classes"] is the list of possible class names (always two)
#
# and a test_data dictionary that has objects and classes entries in the same format as above. It
# should return a list of the same length as test_data["objects"], where the i-th element of the result
# list is the estimated classlabel for test_data["objects"][i]
#
# Do not change the return type or parameters of this function!
#

def word_given_true(word):
   
    if word in true_words.keys():
        freq = true_words[word]
        if freq < 10:
            return 1
        ans = (freq + 0.3)/(total_true_words + 0.3*(distinct_true_words))
        if ans == 0:
            print(word)
        return ans
    
    return 1

def word_given_false(word):

    if word in false_words.keys():
        freq = false_words[word]
        if freq < 10:
            return 1
        ans = (freq + 0.3)/(total_false_words + 0.3*(distinct_false_words))
        if ans == 0:
            print(word)
        return ans
    
    return 1


def result(sentence,vals):

    true_words = vals[0]
    false_words = vals[1]
    true_lines = vals[2]
    false_lines = vals[3]
    total_true_words = vals[4]
    total_false_words = vals[5]

    list_words = preprocess(sentence)
    
    p_true = 0
    p_false = 0

    total_true_words += len(true_words)*0.3
    total_false_words += len(false_words)* 0.3

    

    for word in list_words:
        ft = 0
        if word in true_words.keys():
            ft = true_words[word]
        ff = 0
        if word in false_words.keys():
            ff = false_words[word]
        p_true += math.log2((0.3 + ft)/total_true_words)
        p_false += math.log2((0.3 + ff)/total_false_words)
    
    total = true_lines + false_lines
    true = true_lines/(total) 
    false = 1- true
    
    p_true += math.log2(true)
    p_false += math.log2(false)

    if (p_true > p_false):
        return "truthful"
    else:
        return "deceptive"    


import string 

def preprocess(line):

   line = line.lower()
   line = line.translate(str.maketrans('', '', string.punctuation))
   words = line.strip().split(" ")
   #print(words)
   return words

def classifier(train_data, test_data):
    
    true_words = {}
    false_words = {}
    distinct_true_words =0
    distinct_false_words = 0
    true_lines = 0
    false_lines = 0
    total_true_words = 0
    total_false_words = 0
    true = 0
    false = 0

    for i in range(len(train_data["objects"])):
        processed_words = preprocess(train_data['objects'][i])
        if train_data['labels'][i] == "truthful":
            true_lines += 1
            total_true_words += len(processed_words)
            for j in processed_words:
                if j not in true_words:
                    true_words[j] = 1
                else :
                    true_words[j] += 1

        else:
            false_lines += 1
            total_false_words += len(processed_words)
            for j in processed_words:
                if j not in false_words:
                    false_words[j] = 1
                else :
                    false_words[j] += 1

    distinct_true_words = len(true_words)
    distinct_false_words = len(false_words)

    
    vals = []
    vals.append(true_words)
    vals.append(false_words)
    vals.append(true_lines)
    vals.append(false_lines)
    vals.append(total_true_words)
    vals.append(total_false_words)


    res = []

    for i in range(len(test_data["objects"])):
       ans = result(test_data["objects"][i],vals)
       res.append(ans)
    return res


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise Exception("Usage: classify.py train_file.txt test_file.txt")

    (_, train_file, test_file) = sys.argv
    # Load in the training and test datasets. The file format is simple: one object
    # per line, the first word one the line is the label.
    train_data = load_file(train_file)
    test_data = load_file(test_file)
    if(sorted(train_data["classes"]) != sorted(test_data["classes"]) or len(test_data["classes"]) != 2):
        raise Exception("Number of classes should be 2, and must be the same in test and training data")

    # make a copy of the test data without the correct labels, so the classifier can't cheat!
    test_data_sanitized = {"objects": test_data["objects"], "classes": test_data["classes"]}

    results= classifier(train_data, test_data_sanitized)

    # calculate accuracy
    correct_ct = sum([ (results[i] == test_data["labels"][i]) for i in range(0, len(test_data["labels"])) ])
    print("Classification accuracy = %5.2f%%" % (100.0 * correct_ct / len(test_data["labels"])))
