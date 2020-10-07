---
layout: post
title: One result ...several questions
date: 2020-08-11
---

<!-- wp:paragraph -->

At this point we have tokenized the whole text of the "World Messianic Bible" and we have the first report of the most used words that are also semantically valuable:" LORD", "shall" and "said" are the first of 2362 unique token-words found.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

The API service that provided us with the text has listed 23 English available versions of the bible, and it claims to provide 2500 versions in over 1600 languages.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

I wonder how the token list will vary depending on the version we use and even other languages, I'm particularly interested in checking whether NLTK provides support for Hebrew or not.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Another thing we can get is the most used words by each book, which could give us some insight into the main topic of each one.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

For the word-token frequency by book, we can run:

<!-- /wp:paragraph -->

<!-- wp:syntaxhighlighter/code -->
<pre class="wp-block-syntaxhighlighter-code">SELECT book,token, count(*) as 'count' FROM wordtokens GROUP BY book,token ORDER by 1,3 desc;</pre>
<!-- /wp:syntaxhighlighter/code -->

<!-- wp:paragraph -->

Which give us the following results (**f_e_print_word_frequency_by_book.py**):

<!-- /wp:paragraph -->

<!-- wp:syntaxhighlighter/code -->
<pre class="wp-block-syntaxhighlighter-code">1CH	sons(303)		David(181)		LORD(172)		
1CO	things(76)		Messiah(66)		Lord(66)		
1JN	know(36)		us(35)		love(35)		
1KI	LORD(252)		said(207)		Israel(194)		
1PE	Messiah(19)		may(14)		also(13)		
1SA	LORD(309)		Saul(288)		David(281)		
1TH	Lord(25)		Yeshua(17)		us(16)		
1TI	good(22)		faith(17)		Messiah(16)		
2CH	king(248)		house(194)		God(181)		
2CO	Messiah(47)		also(45)		us(43)		
2JN	Father(4)		us(3)		teaching(3)		
2KI	LORD(276)		said(221)		Israel(149)		
2PE	things(12)		day(10)		Yeshua(9)		
2SA	David(274)		said(230)		LORD(142)		
2TH	God(19)		Yeshua(12)		us(9)		
2TI	Yeshua(14)		Messiah(14)		God(13)		
3JN	brothers(3)		God(3)		write(2)		
ACT	said(149)		Paul(126)		Lord(98)		
AMO	says(46)		Israel(26)		house(25)		
COL	God(22)		things(20)		also(15)		
DAN	Daniel(72)		God(48)		kingdom(47)		
DEU	LORD(545)		God(341)		land(179)		
ECC	God(39)		time(38)		heart(36)		
EPH	God(31)		one(24)		Lord(24)		
EST	Mordecai(56)		Esther(53)		Haman(51)		
EXO	LORD(385)		Moses(283)		said(199)		
EZK	Lord(221)		says(209)		LORD(191)		
EZR	God(95)		king(63)		hundred(60)		
GAL	law(30)		God(30)		faith(19)		
GEN	father(260)		God(214)		land(190)		
HAB	nations(7)		like(7)		violence(5)		
HAG	says(20)		Hosts(13)		son(10)		
HEB	things(38)		made(30)		faith(30)		
HOS	LORD(37)		Israel(37)		Ephraim(24)		
ISA	shall(192)		like(162)		says(109)		
JAS	God(17)		faith(16)		brothers(14)		
JDG	Israel(172)		LORD(169)		children(128)		
JER	says(337)		king(226)		land(190)		
JHN	Yeshua(238)		therefore(100)		answered(77)		
JOB	man(77)		Job(54)		know(53)		
JOL	children(11)		great(10)		God(10)		
JON	said(18)		Jonah(18)		God(14)		
JOS	children(190)		Joshua(155)		Israel(153)		
JUD	ungodly(5)		Yeshua(5)		God(5)		
LAM	daughter(20)		like(14)		day(14)		
LEV	LORD(284)		offering(268)		priest(183)		
LUK	Yeshua(96)		son(89)		saying(72)		
MAL	says(27)		Hosts(18)		say(13)		
MAT	Yeshua(158)		saying(94)		came(93)		
MIC	like(19)		come(15)		people(12)		
MRK	Yeshua(84)		came(75)		went(47)		
NAM	like(12)		away(7)		make(5)		
NEH	son(112)		God(71)		hundred(49)		
NUM	LORD(385)		children(258)		offering(242)		
OBA	possess(6)		LORD(6)		Esau(6)		
PHM	Messiah(6)		fellow(4)		Paul(4)		
PHP	things(25)		God(22)		Yeshua(19)		
PRO	wicked(75)		LORD(74)		shall(61)		
PSA	God(321)		shall(183)		like(146)		
REV	earth(76)		great(61)		like(60)		
ROM	law(73)		Messiah(63)		also(60)		
RUT	Naomi(22)		Boaz(20)		LORD(18)		
SNG	beloved(32)		love(20)		beautiful(13)		
TIT	things(10)		good(10)		may(9)		
ZEC	Hosts(51)		says(42)		Jerusalem(35)	</pre>
<!-- /wp:syntaxhighlighter/code -->

<!-- wp:paragraph -->

Next, lets try with other English translation, for that we just need to change the BIBLE_ID parameter and run all our scripts again:

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

In **`c_a_parameters_bible.py`** we put the id for : **`bf8f1c7f3f9045a5-01'JPS TaNaKH 1917`**

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

And we run the next scripts:

<!-- /wp:paragraph -->

<!-- wp:syntaxhighlighter/code -->
<pre class="wp-block-syntaxhighlighter-code">python c_b_retrieve_bible_books.py 
python d_b_retrieve_books_chapters.py 
python e_b_retrieve_chapters_text.py
python f_b_tokenize_documents.py
</pre>
<!-- /wp:syntaxhighlighter/code -->

<!-- wp:paragraph -->

Which result in the following list of tokens by frequency:

<!-- /wp:paragraph -->

<!-- wp:syntaxhighlighter/code -->
<pre class="wp-block-syntaxhighlighter-code">('shall', 7404)
('unto', 6820)
('LORD', 6535)
('thou', 3356)
('thy', 3317)
('said', 2899)
('thee', 2879)
('God', 2654)
('Israel', 2505)
('upon', 2451)
('king', 2410)
('ye', 2314)
('son', 1897)
('land', 1838)
</pre>
<!-- /wp:syntaxhighlighter/code -->

<!-- wp:paragraph -->

Which shows that NLTK does not have words like "thou" or "thy" in its list of stop-words. It does allow for editing that list though, so is a solvable issue.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Next, a tougher test: Hebrew

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

<!-- /wp:paragraph -->