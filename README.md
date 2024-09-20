# text-processing-examples
Simple text processing scripts for a Huminfra handbook chapter.

## Lemmatisation with efselab
We here showcase how [pefselab](https://github.com/skogsgren/pefselab) is used for lemmatising our example data.

Follow [pefselab's'](https://github.com/skogsgren/pefselab) instructions. Also, make sure you have a new enough version of Python.

To run the code here, you also need nltk. (With e.g., conda: `conda install anaconda::nltk`).

You first need to run `create_pefselab_pipeline.py` once, to create the NLP pipeline. Then you can run the script for lemmatisation `lemmatise_motions.py`.

The script expects one folder with ".txt"-files (the first argument to the script) as well as the name of the folder where the lemmatised files are to be positioned. (See `run_lemmatise_motions.sh` for an exampel of how to run the script.)

 
