## [LuLu](https://lulu.com)
I use LuLu alot.  I love LuLu.  Sometimes I just want to print something out and throw it in my 
backpack to take on a flight and I need it now.  That is when I print at home.  If I am in no rush 
I create a project in LuLu and when I have enough things in my cart to justify paying for shipping 
I order.

## Printing at home

### LaTeX
I use [texlive]([url](https://www.tug.org/texlive/)) on Fedora:
```bash
sudo dnf install texlive-scheme-full
```

### Generating the booklet PDF
Start off with a PDF meant for reading or printing "normal", not in a booklet and process it with
`pdfjam`.  `pdfjam` is a addon for LaTex.  You can read about its use for booklets in 
[using pdfjam for zine creation](https://web.archive.org/web/20220504031424/https://equa.space/notes/pdfjam/),
or get more info about pdfjam at the [author's GitHub](https://github.com/rrthomas/pdfjam).

I am using A4 paper.  The office supply stores in the US don't have A4, but Amazon does, and at $10 for 
500 sheets I think it is worth it since there are many zines and pamphlets designed for A5, and A5 is
half of A4.

```bash
pdfjam Runequest.pdf --booklet true --paper a4 --landscape --outfile rune-a5.pdf
```

### Printing from Document Viewer on Fedora
These settings may work out from other operating systems or tools, or maybe not.  This works for printing to
a Brother MFC-xxxxx with A4 paper loaded in the Multi-purpose tray (the one on the back of the printer, not
the tray under the printer).

#### Page Setup tab
In the screenshot you can see that I bumped the scale up to 112%.  This will vary based on the PDF that you start
from, the paper size, and the phase of the moon.  I hit the **Preview** button in Document Viewer, saw that there
was a big margin around the edges and adjusted.

![image](https://user-images.githubusercontent.com/25182304/193430007-182d382d-2e6c-4823-a459-cd814c9f3c1f.png)

#### Page handling tab

![image](https://user-images.githubusercontent.com/25182304/193430024-a662459a-6ebd-47a0-8f45-8aa1c13e1431.png)
