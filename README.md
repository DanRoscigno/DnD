# DnD

Uses [dungeonsheets](https://github.com/canismarko/dungeon-sheets)
To update: 
```
sudo pip3 install \
  https://github.com/canismarko/dungeon-sheets/archive/refs/heads/master.zip
```

Uses [DND 5E LaTeX Template](https://github.com/rpgtex/DND-5e-LaTeX-Template)

I run in a GCP cheapo VM.  Create an N1 VM and select the f1-micro (1 vCPU, 0.6 GB memory) machine type.  Use Debian 10 with a 20GB boot disk (probably 15 would do, but 10 GB is too small unless you want to install TeX by hand).

### Here are the commands I ran:
```
sudo apt-get install python3-pip
sudo apt-get install texlive-full
sudo apt-get install wget unzip git
sudo pip3 install dungeonsheets
kpsewhich -var-value TEXMFHOME
mkdir -p "$(kpsewhich -var-value TEXMFHOME)/tex/latex/"
wget https://github.com/rpgtex/DND-5e-LaTeX-Template/archive/master.zip
unzip -d "$(kpsewhich -var-value TEXMFHOME)/tex/latex/" master.zip
cd "$(kpsewhich -var-value TEXMFHOME)/tex/latex/"
mv DND-5e-LaTeX-Template-master dnd
sudo apt-get install pdftk
cd
git clone https://github.com/DanRoscigno/DnD.git
cd DnD
cd characters/
makesheets -F darvas-level-3.py
```

### Download the PDF
Click on the star icon at top of GCP ssh browser window and select 
Download file, this is the file (based on my home dir):
`/home/dan_roscigno/DnD/characters/darvas-level-3.pdf`
