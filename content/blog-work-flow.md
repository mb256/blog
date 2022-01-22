Title: Blog howto (Pelican + github pages)
Date: 2021-11-20 12:20
Modified: 2021-11-20 13:00
Category: tech
Tags: tech, pelican, blog, github pages, hosting static html
Slug: pelican-github-workflow
Authors: mb256
Summary: How to make free blog on github with Pelican (static site generator). 

I was looking for blog platform for quite a long time before I give it to try [Pelican](https://github.com/getpelican/pelican) generator (other [link](https://blog.getpelican.com)). Pelican is static html content generator and via this tool there is possible to generate html and hosts them on gihub [pages](https://pages.github.com).   

There are several tutorials how to install and setup Pelican project to work properly with github pages.
For example:   

* [Create blog with pelican and github pages](https://rsip22.github.io/blog/create-a-blog-with-pelican-and-github-pages.html)   
* [How to use Pelican on Github pages](https://gist.github.com/JosefJezek/6053301)   
   

At first create new project on github (don't forget to activat github pages :-) ) and clone your project locally. Your 'development' branch will be branch **source**. So create it like this:   
```
git checkout -b source
``` 
   

The output html files (the blog visible for public) will be pushed into **main** (previously **master**) branch. So we need to keep this branch clean.   

   

Is it usefull to use **pelican** tool is python tool and it's useful, safe and recomended to use virtual environment. So setup your virtual env (with Python3 as default python interpreter) and activate it (**blog** environmnet in my case).   

#### Install pelican tool 

We install **pelican** together with **markdown** support and **github pages** support via pip tool:
```
(blog)$ pip install pelican markdown ghp-import
```

#### Create pelican projet
```
(blog)$ pelican-quickstart
```

#### Blog setup

```
> Where do you want to create your new web site? [.] ./
> What will be the title of this web site? Renata's blog
> Who will be the author of this web site? Renata
> What will be the default language of this web site? [pt] en
> Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) n
> Do you want to enable article pagination? (Y/n) y
> How many articles per page do you want? [10] 10
> What is your time zone? [Europe/Paris] America/Sao_Paulo
> Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n) Y **# PAY ATTENTION TO THIS!**
> Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n) n
> Do you want to upload your website using FTP? (y/N) n
> Do you want to upload your website using SSH? (y/N) n
> Do you want to upload your website using Dropbox? (y/N) n
> Do you want to upload your website using S3? (y/N) n
> Do you want to upload your website using Rackspace Cloud Files? (y/N) n
> Do you want to upload your website using GitHub Pages? (y/N) y
> Is this your personal page (username.github.io)? (y/N) y
Done. Your new project is available at /home/username/YOUR_USERNAME.github.io
```

#### Activate virtual environment for this blog:
```
(blog)$ workon blog
```

#### Create new blog post inside 

Create new markdown file (with .md sufix) inside ./content folder with this structure with this content:
```
Title: 
Date: 2021-11-20 12:20
Modified: 2021-11-20 13:00
Category: 
Tags: 
Slug: 
Authors: 
Summary: 

... text of the post ...

```


#### (Re)generate the html content (websites)
```
(blog)$ make html
```

#### Start html server locally on address [localhost:8000]()
```
(blog)$ make serve
```

#### Commit and push actual state of local project into github pages and make them public
```
(blog)$ make github
```

#### More tips and tricks
   

##### Relative URLs on github pages

To use Pelican themes on github pages it's necessary to activate RELATIVE_URLS. Add inside 'pelicanconf.py' config file:
```
RELATIVE_URLS = True
```

##### Replacing theme on github

If you change theme and push it to github pages by (make github) than it's necessary to wait some time (1 - 4 minutes) before you are able to see new theme online (I don't know why - some github cash probably ...)

##### Whole basic config file

```
AUTHOR = 'mb256'
SITENAME = "mb256's blog"
SITEURL = ''

PATH = 'content'
OUTPUT_PATH = 'output'
THEME = '../pelican-themes/bootstrap2-dark'

RELATIVE_URLS = True

STATIC_PATHS = ['images']

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('mbrouk', 'https://mbrouk.pythonanywhere.com/'),
                 ('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

```

##### Display static images

You need to use this configuration in your pelicanconf.py config file to be able to search images inside **images** folder.
```
STATIC_PATHS = ['images']
```

Than you can reference images in markdown like:
```
![Image description]({static}/images/IMAGE_NAME.jpg)
```

