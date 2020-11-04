---
title: Processing PDF Files
published: true
date: 2020-11-03
---

Up to this point, we have been able to extract topics from the bible taking each chapter as an `article` and then extracting topics from the `collection of articles`.

But the initial purpose of this little project of mine was to process and analyze PDF books/articles/papers in bulk; so, let's start playing with one PDF file:

>The Creation Account
>in Genesis 1:1-3
> Part I: Introduction to Biblical Cosmogony
> Bruce K. Waltke

[This site](https://medium.com/better-programming/how-to-convert-pdfs-into-searchable-key-words-with-python-85aab86c544f) has instructions on processing a PDF file, with some changes in punctuation handling it served as a base to make a couple of Experiments:

**Experiment 1**: Out of the 10 topics extracted from the bible, where does this article fits better?

The script in `b_evaluate_for_topics.py` extracts the text from each page of the PDF document and tries to fit it into the topis of the bible model.

First, it prints the topics of the loaded model:

```
[
(0, '0.037*"God" + 0.020*"us" + 0.016*"LORD" + 0.013*"like" + 0.010*"earth" + 0.010*"shall" + 0.009*"make" + 0.009*"heart" + 0.008*"one" + 0.008*"people"'), 
(1, '0.021*"God" + 0.017*"LORD" + 0.012*"like" + 0.012*"also" + 0.011*"Israel" + 0.010*"give" + 0.009*"would" + 0.009*"make" + 0.008*"hear" + 0.008*"people"'), 
(2, '0.027*"LORD" + 0.013*"man" + 0.013*"hand" + 0.012*"like" + 0.009*"wicked" + 0.008*"remember" + 0.008*"fear" + 0.008*"give" + 0.008*"whose" + 0.008*"works"'), 
(3, '0.020*"LORD" + 0.013*"let" + 0.012*"land" + 0.011*"also" + 0.010*"give" + 0.010*"one" + 0.009*"God" + 0.009*"make" + 0.009*"come" + 0.008*"waters"'), 
(4, '0.053*"LORD" + 0.018*"shall" + 0.015*"love" + 0.013*"soul" + 0.013*"God" + 0.010*"praise" + 0.009*"like" + 0.009*"kindness" + 0.008*"wicked" + 0.007*"make"'), 
(5, '0.017*"God" + 0.014*"like" + 0.011*"may" + 0.010*"man" + 0.010*"us" + 0.010*"also" + 0.009*"adversary" + 0.009*"help" + 0.009*"speak" + 0.008*"heart"'), 
(6, '0.077*"LORD" + 0.019*"God" + 0.014*"King" + 0.013*"glory" + 0.010*"lift" + 0.010*"praise" + 0.010*"go" + 0.009*"come" + 0.009*"holy" + 0.008*"make"'), 
(7, '0.049*"God" + 0.036*"LORD" + 0.023*"Praise" + 0.017*"praise" + 0.011*"name" + 0.009*"Lord" + 0.009*"earth" + 0.008*"among" + 0.007*"enemy" + 0.007*"go"'), 
(8, '0.057*"LORD" + 0.037*"love" + 0.037*"endure" + 0.036*"kindness" + 0.029*"forever" + 0.015*"make" + 0.014*"give" + 0.014*"thanks" + 0.010*"earth" + 0.009*"hand"'), 
(9, '0.028*"LORD" + 0.021*"shall" + 0.010*"like" + 0.010*"God" + 0.010*"come" + 0.009*"also" + 0.007*"wicked" + 0.006*"walk" + 0.006*"poor" + 0.006*"men"')
]
```

And then prints the results for each page:

```
[(0, 0.3629536), (2, 0.06154353), (3, 0.13569452), (4, 0.18171218), (5, 0.02853577), (7, 0.07976529), (9, 0.14443298)]
[(0, 0.3347771), (1, 0.06519676), (2, 0.06670042), (3, 0.114596285), (4, 0.2724336), (5, 0.01935592), (7, 0.05632029), (9, 0.068617746)]
[(0, 0.3311244), (1, 0.08430317), (2, 0.039565254), (3, 0.0875445), (4, 0.3193608), (5, 0.0135644255), (7, 0.0651109), (9, 0.058227815)]
[(0, 0.2753348), (1, 0.06866669), (2, 0.036884036), (3, 0.06624074), (4, 0.40929767), (7, 0.047926836), (8, 0.014804971), (9, 0.07104607)]
[(0, 0.2737614), (1, 0.08043589), (2, 0.044808585), (3, 0.061690766), (4, 0.4191902), (7, 0.028765174), (8, 0.011427427), (9, 0.07186866)]
[(0, 0.2654357), (1, 0.084966056), (2, 0.045139376), (3, 0.06016506), (4, 0.41319087), (5, 0.01531588), (7, 0.026706219), (9, 0.07100147)]
[(0, 0.28130144), (1, 0.07700254), (2, 0.046932366), (3, 0.06417108), (4, 0.38586226), (5, 0.017840939), (6, 0.014745815), (7, 0.026398854), (8, 0.012064806), (9, 0.07367994)]
[(0, 0.32041866), (1, 0.06775758), (2, 0.04075425), (3, 0.05423845), (4, 0.37543994), (5, 0.015880177), (6, 0.011993988), (7, 0.024916356), (8, 0.016332861), (9, 0.072267786)]
[(0, 0.3477469), (1, 0.0602976), (2, 0.04229355), (3, 0.04837305), (4, 0.34678146), (5, 0.01804944), (7, 0.020806395), (8, 0.016967317), (9, 0.08896918)]
[(0, 0.32703704), (1, 0.0531322), (2, 0.03943322), (3, 0.051252298), (4, 0.35356033), (5, 0.020715296), (7, 0.031999864), (8, 0.024291242), (9, 0.08896453)]
[(0, 0.32945493), (1, 0.055813164), (2, 0.03439904), (3, 0.05008162), (4, 0.35462666), (5, 0.02404972), (7, 0.03515229), (8, 0.023593834), (9, 0.085034326)]
[(0, 0.3237168), (1, 0.055702135), (2, 0.029051967), (3, 0.048463874), (4, 0.3527789), (5, 0.02531136), (7, 0.0477183), (8, 0.028195716), (9, 0.08122806)]
[(0, 0.32231972), (1, 0.055397317), (2, 0.029504638), (3, 0.048233494), (4, 0.35280898), (5, 0.02510931), (7, 0.04741837), (8, 0.028042614), (9, 0.08341561)]
```
which could be interpreted as:

pages 1, 2, and 3 fit better on Topic-0: God, us, LORD, like, earth, shall, make, heart, one, people

Pages 4, 5, 6, 7, 8, 10, 11, 12, and 13 in topic-4: LORD, shall, love, soul, God, praise, like, kindness, wicked, make

Page 9 is almost equally fitted in Topics 0 and 4

So, `limited` to the 10 main topics of the bible we could say **without actually having read** the article from Dr. Waltke, that:

* While `God, Lord, like, make, shall` are common ideas for the whole text
* the first 3 pages deal more specifically with: `us, earth, one, people`
* and the rest of the article speaks more of: `love, soul, praise, kindness, wicked`

 
But what if the article introduces new ideas/words beyond what we found in the bible topics analysis?
(which seems probable, seeing that the percent/probability of fitting goes only up to ~40%)

**Experiment 2**: Extracting Topics from the PDF itself `a_process_pdf.py`.

Since the process requires a `collection of articles` and the library that extracts text from the PDF file separates the document into pages, each page was considered as an article

```
(0, '0.001*"myth" + 0.001*"creation" + 0.001*"God" + 0.001*"world"')
(1, '0.001*"world" + 0.001*"creation" + 0.001*"myth" + 0.001*"make"')
(2, '0.008*"creation" + 0.008*"world" + 0.007*"myth" + 0.006*"question"')
(3, '0.001*"creation" + 0.001*"myth" + 0.001*"world" + 0.001*"question"')
(4, '0.001*"creation" + 0.001*"world" + 0.001*"myth" + 0.001*"question"')
```

in these results, we can see that the predominant topic would be: `myth, creation, God, world`



| Previous        | Home          | Next |
|:-------------|:------------------|:------|
|  [Topic Modeling](A-topic-visualization) | [θεόφιλος Journey](A-θεόφιλος-Journey) |  |
