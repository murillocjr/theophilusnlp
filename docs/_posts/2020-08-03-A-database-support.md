---
layout: post
title: Database support
date: 2020-08-03
---

<!-- wp:paragraph -->

Since a lot of the data retrieved from the API comes in JSON format, and NLTK outputs are also in JSON, it stands to reason to use a JSON Documents based database to store the partial results and help to process and analyze the data, something on the line of MongoDB or CouchDB; but these two feels like overkill, so TinyDB looks more appropriate for the task at hand, installing it is as simple as:

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

pip install tinydb

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

At this point, it was necessary to do significant modifications to retrieve the whole text of the selected version of the bible, store the data inside TinyDB, and also retrieve the whole text of a Chapter. All the associated code and the resulting databases are available at the following GitHub repo:&nbsp;[https://github.com/murillocjr/theophilusnlp](https://github.com/murillocjr/theophilusnlp)

<!-- /wp:paragraph -->