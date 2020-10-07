---
layout: post
title: Milestone 1
date: 2020-08-04
---

<!-- wp:paragraph -->

This is what we have so far:

<!-- /wp:paragraph -->

<!-- wp:list -->

*   Data: A whole bible text inside TinyDB documents database entities.
*   Code: A function that returns the raw text of a whole chapter on receiving the ChapterID
*   NLTK environment up and running.
<!-- /wp:list -->

<!-- wp:paragraph -->

The code used to retrieve this information is inside small python scripts available on the GitHub repo associated with this project. Since the data is stored in a database we can query it any way we want; also the chapter data is in a JSON format that also can give us paragraphs and verses individually

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Here's where the fun begins; we can start playing with query and code to start gaining insights in the data we have:

<!-- /wp:paragraph -->

<!-- wp:syntaxhighlighter/code -->
<pre class="wp-block-syntaxhighlighter-code">python d_d_print_books_chapters.py ' wc -l
1255</pre>
<!-- /wp:syntaxhighlighter/code -->

<!-- wp:paragraph -->

We can see that there are 1255 chapters that we will treat as separate documents, so in the end, we could get what is the main topic(s) in any particular chapter/document.

<!-- /wp:paragraph -->