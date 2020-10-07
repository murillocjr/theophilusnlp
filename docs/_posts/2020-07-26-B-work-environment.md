---
layout: post
title: [Work environment]
date: 2020-07-26
---

As with most projects, one of the first steps to take is to set up a working environment, since I want to read and take notes on some books and other PDF documents I'll try "I Librarian". Being an open-source software it's possible to set it up on any Linux server, it doesn't seem that it takes a lot of resources either, so an f1-micro VM (Free!) on Google Cloud Platform should be enough to host it.

Using a Debian as the base system, installing I Librarian was pretty straightforward, only thing is that such setup is designed to serve by default at 127.0.0.1, it was necessary accessing it using a tunneling port 80 from my computer:

```bash
sudo ssh -L 80:localhost:80 -i ~/.ssh/gcp-lzrdc lzrd@34.72.155.167
```

Also "my" computer is another cloud instance, also free, but in Amazon (AMI 2 with Mate accessible via VNC)

Why this last Amazon VM?... it's a long story, including a chapter where my only available hardware is a very old HP Semptron 32 bits laptop with no hard drive that miraculously works perfectly if you only run a VNC client, it's funny if you consider COVID-19 lockdown, but I guess you had to be there.

Since yet another VM on AWS is serving as my "processing" unit to run python NLP and text-processing code, the need arises to connect to this headless server, ssh from my "Desktop UI" instance works great with MidnightCommander (mc) along with Micro (text editor) giving me a very easy and confortable way to browse folders and edit files using only the terminal end even with mouse integration.
 
# [](#header-5)UPDATE:

Later I realized that a simple flag on Google VM Instance and a change in the configuration of the virtual service config file allows me to use I Librarian directly pointing to the VM public IP; which is cool because I can now read the PDFs from my phone. Also I librarian seems to have some kind of AI plugin that I need to check later.

# [](#header-5)NOTE: 

Since English is not my first language (which could be obvious by now), I'm using the help of Grammarly to help me while writing these posts.

| Previous        | Home          | Next |
|:-------------|:------------------|:------|
| [Walked Paths](A-walked-paths)          | [θεόφιλος Journey](A-θεόφιλος-Journey) | [Reading the First Document](C-reading-the-first-document)  |
