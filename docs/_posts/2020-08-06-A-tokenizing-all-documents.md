---
layout: post
title: Tokenizing all documents
date: 2020-08-06
---

<!-- wp:paragraph -->

The purpose is to go chapter by chapter and run the "tokenizing by words" process, then store the results in a database so we can start getting statistics on the words used.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

All our JSON documents are stored in TinyDB structures, from there we will extract information like token words; since we will need to run SELECT commands with COUNT and GROUP BY options; which is not that straight forward in TinyDB, we will make use of an SQLite auxiliary database for analysis. 

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

The first tokenization attempt (run over Genesis only, to speed the process) returns the following results (scripts **`f_b_tokenize_documents.py`** and **`f_d_print_word_tokens.py`**) :

<!-- /wp:paragraph -->

<!-- wp:syntaxhighlighter/code -->
<pre class="wp-block-syntaxhighlighter-code">(',', 3802)
('the', 2226)
('and', 1712)
('.', 1460)
('of', 1315)
('to', 1076)
('his', 580)
(''', 567)
('you', 559)
('in', 542)
('"', 537)
('"', 524)
('said', 466)
('I', 439)
('will', 412)
('that', 392)
('him', 386)
('your', 357)
('a', 355)
('he', 348)
('my', 334)
('s', 330)
('was', 316)
('with', 310)
('for', 303)
('is', 278)
('He', 273)
('me', 271)
('father', 260)
('The', 254)
('be', 217)
('God', 214)
</pre>
<!-- /wp:syntaxhighlighter/code -->

<!-- wp:paragraph -->

The total count of unique tokens/words is 43518, from which we can see some issues :

<!-- /wp:paragraph -->

<!-- wp:list -->

*   3802 instances of "," (comma)
*   2226 instances of "the", etc
<!-- /wp:list -->

<!-- wp:paragraph -->

which won't be useful at this stage of Topic Modeling, so we need to prevent these "stop words" and punctuation symbols to get into the database; NLTK provides help for this task with:

<!-- /wp:paragraph -->

<!-- wp:syntaxhighlighter/code -->
<pre class="wp-block-syntaxhighlighter-code">stop_words = set(stopwords.words('english'))

tokens = word_tokenize(chapter_text)
    non_punctuation_tokens = [token for token in tokens if token.isalnum()]
    removed_stop_words = [w for w in non_punctuation_tokens if not w.lower() in stop_words] 
</pre>
<!-- /wp:syntaxhighlighter/code -->

<!-- wp:paragraph -->

Which reduces the count to 2362 (~ 5.43% of the first list) remaining token words:

<!-- /wp:paragraph -->

<!-- wp:syntaxhighlighter/code -->
<pre class="wp-block-syntaxhighlighter-code">('said', 466)
('father', 260)
('God', 214)
('land', 190)
('Jacob', 175)
('LORD', 162)
('Joseph', 152)
('son', 146)
('sons', 136)
('Abraham', 132)
...</pre>
<!-- /wp:syntaxhighlighter/code -->

<!-- wp:paragraph -->

So....: there's a lot "said" in Genesis    :)

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Releasing the tokenization for all the chapters in the bible we get:

<!-- /wp:paragraph -->

<!-- wp:syntaxhighlighter/code -->
<pre class="wp-block-syntaxhighlighter-code">('LORD', 6189)
('shall', 4318)
('said', 3819)
('God', 3540)
('Israel', 2352)
('king', 2346)
('one', 2129)
('man', 2035)
('son', 2031)
('people', 1793)
('house', 1746)
('children', 1722)
('came', 1648)
('land', 1632)
('men', 1444)
</pre>
<!-- /wp:syntaxhighlighter/code -->

<!-- wp:paragraph -->

This first result could be interpreted as a very, very rough answer to "What the bible talks about?" and it has a very deep meaning for me personally.

<!-- /wp:paragraph -->