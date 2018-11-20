#-*- coding: utf-8 -*-

"""

    ->      make html tag        <-

"""


def make_html_tag(text, tag):
	return '<%s>%s</%s>' %(tag,text,tag)

print make_html_tag('il mio testo per il titolo', 'title')
print make_html_tag('riga in grossetto', 'bold')