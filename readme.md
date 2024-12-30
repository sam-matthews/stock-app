# Readme

## Loading DDL statements via JSON or YAML

A bit of research with this one. I had started by using JSON files. However for reasons shown below I have decided to move to yaml files.

1. JSON Files are completed.
2. JSON files do not support Multiline values.

> With this in mind I have decided to use yaml, or at least trial storing this data in yaml configuraiton files. **Note:** There is one limitation I have found. Working with YAML files does mean that there may be some efficiencies, however this issue generally only occurs when the files get very large.

## Implementation
