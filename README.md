# music-machines
## Simple Chord Progression Generator
Data: one chord per row in a CSV file with "chords" at the top for the header. Name the file "chords.csv".

Usage: `generate_sequence('C',length=5)` will give a chord progression of 5 chords that are likely to follow C.

## Chord Scraper 
### takes comma separated list of urls via command line and scrapes them for chords. 
### must have an empty file called 'output.csv' with one new line at the end
### customized for the e-chords.com website format
Usage: from terminal, run `python3 chord_scraper.py url1, url2, etc`
