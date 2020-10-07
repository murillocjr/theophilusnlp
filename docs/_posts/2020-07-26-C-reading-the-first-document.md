---
layout: post
title: Reading the first document
date: 2020-07-26
---

Started reading

Debortoli, Stefan; Müller, Oliver; Junglas, Iris; and vom Brocke, Jan (2016) `"Text Mining For Information Systems Researchers: An Annotated Topic Modeling Tutorial,"` Communications of the Association for Information Systems: Vol. 39, Article 7. DOI: 10.17705/1CAIS.03907 Available at [http://aisel.aisnet.org/cais/vol39/iss1/7](http://aisel.aisnet.org/cais/vol39/iss1/7)

Looks promising, it goes along with my idea of a practical application and example with theoretical support, good references, and example cases; cool!

Based on computer science and linguistics is particularly focused on probabilistic topic modeling

Leximancer seems to implement a similar idea, might check it more later to see how they do it

A sufficiently large data set (n > 1,000) will be needed.

Note that an extensive preprocessing phase is necessary before one can statistically analyze data through topic models.

Low-level natural language processing (NLP) steps will be implemented, such as:


###### [](#header-5)tokenization  
Splitting up documents into sentences and sentences into words; n-gram creation: creating n consecutive words: 1-grams include, for example, "fast", "food", or "chain"; 2-grams concatenate two 1-grams, such as "fast food"; and 3-grams comprise three 1-grams, such as "fast food chain"

###### [](#header-5)stopping  
Removing common or uninformative words), partof-speech filtering (i.e., identifying and filtering words by their part of speech

###### [](#header-5)lemmatizing  
Reducing a word into its dictionary form; for example, plural to singular for nouns, verbs to the simple present tense

###### [](#header-5)stemming  
Reducing a word to its stem


Ok, halfway through the document and the practical part starts, so hands on!


Minemytext was the tool used on this publication, this online tool seems pretty neat. Since I want a more hands-on code kind of approach I'll try some toolkits:

[NLP Tools](https://opensource.com/article/19/3/natural-language-processing-tools)

[NLTK](http://www.nltk.org/)
                                                                                                                                            

| Previous        | Home          | Next |
|:-------------|:------------------|:------|
| [Work Environment](B-work-environment) | [θεόφιλος Journey](A-θεόφιλος-Journey) | [NLTK](D-nltk)  |
