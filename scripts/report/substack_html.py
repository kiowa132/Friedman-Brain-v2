import re, html, os
D = r"C:\Users\kylej\Documents\GitHub\friedman-brain\Friedman Brain\drafts\friedman-report"
src = open(os.path.join(D, "2026-09-14-to-09-20", "substack.md"), encoding="utf-8").read()
assert not re.search("[\u2014\u2013]", src)
title = re.search(r"TITLE: (.*)", src).group(1)
sub = re.search(r"SUBTITLE: (.*)", src).group(1)
body = src.split("\n---\n", 1)[1].strip().split("\n\n")


def inl(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', t)
    return t


out = []
for b in body:
    if b.startswith("## "):
        out.append("<h2>%s</h2>" % inl(b[3:]))
    elif b.startswith("* "):
        out.append("<ul>" + "".join("<li>%s</li>" % inl(l[2:]) for l in b.split("\n")) + "</ul>")
    elif re.match(r"1\. ", b):
        out.append("<ol>" + "".join("<li>%s</li>" % inl(re.sub(r"^\d+\. ", "", l)) for l in b.split("\n")) + "</ol>")
    elif b.startswith("Have Questions"):
        out.append("<p>" + "<br>".join(inl(l) for l in b.split("\n")) + "</p>")
    elif b.startswith("[Schedule"):
        out += ["<p>%s</p>" % inl(l) for l in b.split("\n")]
    else:
        out.append("<p>%s</p>" % inl(b))

prev = open(os.path.join(D, "2026-09-07-to-09-13", "substack-formatted.html"), encoding="utf-8").read()
head = prev.split('<div class="howto">')[0]
head = re.sub(r"<title>.*?</title>", "<title>Substack paste, Friedman Report, Sep 14-20, 2026</title>", head)
howto = ('<div class="howto"><strong>How to use:</strong> Put the title and subtitle in Substack\'s own fields. '
         'Then select everything below the line (from "Denise and Walt" to the end), copy, and paste into the '
         'Substack editor.<br><br><strong>Title:</strong> %s<br><strong>Subtitle:</strong> %s</div>\n<hr>\n'
         % (html.escape(title), html.escape(sub)))
open(os.path.join(D, "2026-09-14-to-09-20", "substack-formatted.html"), "w", encoding="utf-8").write(
    head + howto + "\n\n".join(out) + "\n")
print("ok")
