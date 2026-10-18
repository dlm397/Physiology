# Watch7 / Samsung Health datasets

## Description

This project began as a simple data archive, as health data from watches, scales, etc. is not kept forever, particularly in the case of high-resolution data. I have been expanding it to include some simple analysis, for my own benefit, as well as particing N-of-1 techniques.

## Layout

```text
Data/                          All contents are kept private
  raw/                         Original imports; read-only inputs
  datasets/                    Finished datasets and their dictionaries
  scripts/                     Parsers, builders, and loaders 
    tests/                     Python tests
    validation/                Stata checks
  logs/                        Reorganization checks and execution logs
  backups/                     Historical builds and old files
Output/                        Products of data analysis
requirements.txt               Python dependencies
README.md                      This dataset catalog and usage guide
```
