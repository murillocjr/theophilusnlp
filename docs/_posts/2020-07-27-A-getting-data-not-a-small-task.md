---
layout: post
title: Getting data...not a small task
date: 2020-07-27
---

<!-- wp:paragraph -->

We need data:

<!-- /wp:paragraph -->

<!-- wp:list -->

*   Text in proper English
*   Available programmatically from python
*   Lots of "articles" that can be processed later, more than 1000 according to the recommendations.
<!-- /wp:list -->

<!-- wp:paragraph -->

Instead of going directly to books, let's start testing with the Bible text because additionally to more or less fit the above requirements, it goes with the theology theme I'm going for, and I guess it will not be so difficult to get all chapters into a database later for massive processing.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

I wonder how the tokenizer will react to the paragraph-long sentences Paul uses a lot on his letters.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

For sandbox test processes lets try Genesis 1, fortunately, there's a service that provides bible portions via an API, allows for free registration to get an api-key, and returns data in text/HTML/JSON, also provides a small set of versions of the bible.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

[https://scripture.api.bible](https://scripture.api.bible)

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

[Message from the future: this API does not provide a bible in Hebrew, so it might have been a good idea to check that first]

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Export the api-key

<!-- /wp:paragraph -->

<!-- wp:syntaxhighlighter/code -->
<pre class="wp-block-syntaxhighlighter-code">export KEY=8...your-key...a</pre>
<!-- /wp:syntaxhighlighter/code -->

<!-- wp:paragraph -->

List of available bibles

<!-- /wp:paragraph -->

<!-- wp:syntaxhighlighter/code -->
<pre class="wp-block-syntaxhighlighter-code">curl -X GET "https://api.scripture.api.bible/v1/bibles?language=eng" -H "api-key:$KEY"</pre>
<!-- /wp:syntaxhighlighter/code -->

<!-- wp:paragraph -->

Which return a long JSON string, in order to have a better look at which versions are available, a small python script will help:

<!-- /wp:paragraph -->

<!-- wp:syntaxhighlighter/code {"language":"python"} -->
<pre class="wp-block-syntaxhighlighter-code">import json

with open('available-bibles.json', 'r') as f:
    bibles_dict = json.load(f)

for bible in bibles_dict['data']:
    print(bible['id'] + ''' + bible['name'])
</pre>
<!-- /wp:syntaxhighlighter/code -->

<!-- wp:paragraph -->

which prints:

<!-- /wp:paragraph -->

<!-- wp:syntaxhighlighter/code -->
<pre class="wp-block-syntaxhighlighter-code">55212e3cf5d04d49-01'Cambridge Paragraph Bible of the KJV
179568874c45066f-01'Douay-Rheims American 1899
55ec700d9e0d77ea-01'English Majority Text Version
65eec8e0b60e656b-01'Free Bible Version
c315fa9f71d4af3a-01'Geneva Bible
bf8f1c7f3f9045a5-01'JPS TaNaKH 1917
de4e12af7f28f599-01'King James (Authorised) Version
de4e12af7f28f599-02'King James (Authorised) Version
40072c4a5aba4022-01'Revised Version 1885
ec290b5045ff54a5-01'Targum Onkelos Etheridge
2f0fd81d7b85b923-01'The English New Testament According to Family 35
06125adad2d5898a-01'The Holy Bible, American Standard Version
66c22495370cdfc0-01'Translation for Translators
9879dbb7cfe39e4d-01'World English Bible
9879dbb7cfe39e4d-02'World English Bible
9879dbb7cfe39e4d-03'World English Bible
9879dbb7cfe39e4d-04'World English Bible
7142879509583d59-01'World English Bible British Edition
7142879509583d59-02'World English Bible British Edition
7142879509583d59-03'World English Bible British Edition
7142879509583d59-04'World English Bible British Edition
f72b840c855f362c-04'World Messianic Bible
04da588535d2f823-04'World Messianic Bible British Edition
</pre>
<!-- /wp:syntaxhighlighter/code -->

<!-- wp:paragraph -->

After picking   
f72b840c855f362c-04'World Messianic Bible  
let's get the books listing:

<!-- /wp:paragraph -->

<!-- wp:syntaxhighlighter/code -->
<pre class="wp-block-syntaxhighlighter-code">curl -X GET "https://api.scripture.api.bible/v1/bibles/f72b840c855f362c-04/books" -H "api-key:$KEY"</pre>
<!-- /wp:syntaxhighlighter/code -->

<!-- wp:syntaxhighlighter/code -->
<pre class="wp-block-syntaxhighlighter-code">{
  "data": [
    {
      "id": "GEN",
      "bibleId": "f72b840c855f362c-04",
      "abbreviation": "Genesis",
      "name": "Genesis",
      "nameLong": "The First Book of Moses, Commonly Called Genesis"
    },
    {
      "id": "EXO",
      "bibleId": "f72b840c855f362c-04",
      "abbreviation": "Exodus",
      "name": "Exodus",
      "nameLong": "The Second Book of Mosis, Commonly Called Exodus"
    },
    {
      "id": "LEV",
      "bibleId": "f72b840c855f362c-04",
      "abbreviation": "Leviticus",
      "name": "Leviticus",
      "nameLong": "The Third Book of Mosis, Commonly Called Leviticus"
    },</pre>
<!-- /wp:syntaxhighlighter/code -->

<!-- wp:paragraph -->

With the obtained book-id we can fetch the chapters:

<!-- /wp:paragraph -->

<!-- wp:syntaxhighlighter/code -->
<pre class="wp-block-syntaxhighlighter-code">curl -X GET "https://api.scripture.api.bible/v1/bibles/f72b840c855f362c-04/books/GEN/chapters" -H "api-key:$KEY"</pre>
<!-- /wp:syntaxhighlighter/code -->

<!-- wp:syntaxhighlighter/code -->
<pre class="wp-block-syntaxhighlighter-code">{
  "data": [
    {
      "id": "GEN.intro",
      "bibleId": "f72b840c855f362c-04",
      "bookId": "GEN",
      "number": "intro",
      "reference": "Genesis"
    },
    {
      "id": "GEN.1",
      "bibleId": "f72b840c855f362c-04",
      "bookId": "GEN",
      "number": "1",
      "reference": "Genesis 1"
    },
    {
      "id": "GEN.2",
      "bibleId": "f72b840c855f362c-04",
      "bookId": "GEN",
      "number": "2",
      "reference": "Genesis 2"
    },</pre>
<!-- /wp:syntaxhighlighter/code -->

<!-- wp:paragraph -->

Now we have enough information to fetch the text of a whole chapter, for our purposes we will retrieve the chapter divided in verses inside a JSON structure

<!-- /wp:paragraph -->

<!-- wp:syntaxhighlighter/code -->
<pre class="wp-block-syntaxhighlighter-code">curl -X GET "https://api.scripture.api.bible/v1/bibles/f72b840c855f362c-04/chapters/GEN.1?content-type=json&include-notes=false&include-titles=false&include-chapter-numbers=false&include-verse-numbers=false&include-verse-spans=false" -H "api-key:$KEY" > GEN.1.json
</pre>
<!-- /wp:syntaxhighlighter/code -->

<!-- wp:syntaxhighlighter/code -->
<pre class="wp-block-syntaxhighlighter-code">{
  "data": {
    "id": "GEN.1",
    "bibleId": "f72b840c855f362c-04",
    "number": "1",
    "bookId": "GEN",
    "reference": "Genesis 1",
    "copyright": "\n          \n            PUBLIC DOMAIN\n          \n        ",
    "content": [
      {
        "name": "para",
        "type": "tag",
        "attrs": {
          "style": "p"
        },
        "items": [
          {
            "text": "In the beginning, God",
            "type": "text",
            "attrs": {
              "verseId": "GEN.1.1",
              "verseOrgIds": [
                "GEN.1.1"
              ]
            }
          },
          {
            "text": " created the heavens and the earth. ",
            "type": "text",
            "attrs": {
              "verseId": "GEN.1.1",
              "verseOrgIds": [
                "GEN.1.1"
              ]
            }
          },
          {
            "text": "The earth was formless and empty. Darkness was on the surface of the deep and God's Spirit was hovering over the surface of the waters.",
            "type": "text",
            "attrs": {
              "verseId": "GEN.1.2",
              "verseOrgIds": [
                "GEN.1.2"
              ]
            }
          }
        ]
      },</pre>
<!-- /wp:syntaxhighlighter/code -->

<!-- wp:paragraph -->

this is the basic information we will be retrieving from the API service.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

<!-- /wp:paragraph -->