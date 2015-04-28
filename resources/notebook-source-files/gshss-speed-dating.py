# <markdowncell>
# <br>
# <img style="float:left" src="http://ipython.org/_static/IPy_header.png" />
# <br>

# <headingcell level=1>
# Speed dating with Python and NLTK

# <markdowncell>
# > Welcome to *Python* and the *IPython Notebook*! Today, we're demonstrating NLTK, a library for working with natural language.

# <headingcell level=2>
# Tell me a little about yourself

# <markdowncell>
# > Whatever your area of study, Python can speed up repetitive tasks and ensure that whatever you do can quickly be redone, by anyone.

# <codecell>
departments = ['History', 'Politics', 'Anthropology', 'Linguistics', 'Psychology']

for department in departments:
    print "You work in the %s department!? How interesting!" % department


# <headingcell level=2>
# What line of work are you in?

# <markdowncell>
# > The NLTK library of Python provides a powerful way of working with **language as data**.

# <codecell>
%run demo.ipy
import nltk
from nltk.book import text4 as speeches

# <codecell>
print speeches[:100]

# <headingcell level=2>
# Fascinating! Tell me more ...

# <markdowncell>
# > We can quickly harvest and visualise information from large bodies of text.

# <codecell>
from nltk.draw import dispersion_plot
speeches.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])

# <headingcell level=2>
# You probably say that to everyone!

# <markdowncell>
# > Of course, you can work with your own texts, too:

# <codecell>
sentence = "Your eyes look beautiful in the moonlight."

# <codecell>
parsetree(sentence)

# <headingcell level=2>
# Let's talk politics ...

# <markdowncell>
# > We have been investigating a corpus of speeches made by Malcolm Fraser between 1954 and 1982. 

# > Every word has been annotated with its word class, and every clause has been annotated with grammatical structure information.

# > Let's search it for modal auxiliaries, like *can*, *may*, *would* and *should*:

# <codecell>
corpus = '../corpora/fraser-corpus-annotated'
modal_words = 'MD'

# <codecell>
modals = interrogator(corpus, 'words', modal_words)

# <codecell>
plotter('Modals in Fraser Speeches', modals.results, fract_of = modals.totals)

# <headingcell level=2>
# Call me, eh?

# <markdowncell>
# > Sign up for free Python, IPython and NLTK lessons!

# <markdowncell>
