from glob import glob
import os
import sys
from pefselab.swe_pipeline import SwedishPipeline
from nltk.corpus import stopwords

to_remove = ["observera dokument inskannad fel förekomma", "Norstedts TRYCKERI", "Göteborg TRYCKERIBOLAGET Ivar HAEGGSTRÖM AB", "Alfa boktryckeri AB", "AB Egneilska boktryckeri",  "Beckman tryckeri AB"]
more_stopwords = ["lil", "nr", "kungl.maj", "majit"]

def lemmatise_motions(corpus_folder, output_folder):
    
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)
    else:
        print("Output folder already exists: ", output_folder,  "\nRemove it and try again")
        sys.exit(1)
        
    files_to_lemmatise = glob(os.path.join(corpus_folder, "*.txt"))
    if len(files_to_lemmatise) == 0:
        print("No files with a 'txt'-suffix found in ", corpus_folder)
        sys.exit(1)
        
    nlp = SwedishPipeline(files_to_lemmatise)
        
    filter_with = stopwords.words("swedish") + more_stopwords

    for key, value in nlp.documents.items():
        file_to_write_to = os.path.join(output_folder, key)

        with open(file_to_write_to, "w") as lemmatised_file:
            lemmatised_text = " ".join([lemma for (lemma, token) in zip(value.lemmas, value.tokens) if lemma.lower() not in filter_with and token.lower() not in filter_with])
            for remove_text in to_remove:
                lemmatised_text = lemmatised_text.replace(remove_text, " ")
            lemmatised_file.write(lemmatised_text.strip())
        

# Start
########
try:
    corpus_folder_arg = sys.argv[1]
    output_folder_arg = sys.argv[2]
 
except IndexError:
    print("The script needs two arguments: The first is the path to the folder where the corpus is located. The second is the path where to output the lemmatised files.")
    sys.exit(1)

lemmatise_motions(corpus_folder = corpus_folder_arg, output_folder = output_folder_arg)
