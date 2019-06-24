#
# index.py
# Whoosh testing
#

import os
from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID
import sys


def createSearchableData(root):

    # Schema definition: title(name of text file), path(as ID),
    # content(indexed, but not stored), textdata(stored text content)
    # schema = Schema(title=TEXT(stored=True),
    #                 content=TEXT, textdata=TEXT(stored=True))
    schema = Schema(title=TEXT(stored=True), content=TEXT,
                    textdata=TEXT(stored=True))

    if not os.path.exists("indexdir"):
        os.mkdir("indexdir")

    # Creating an index writer to add documents
    # as per schema
    ix = create_in("indexdir", schema)
    writer = ix.writer()

    filepaths = [os.path.join(root, i) for i in os.listdir(root)]
    for path in filepaths:
        fp = open(path, 'r')
        print(path)
        text = fp.read()
        writer.add_document(title=path.split("\\")[1],
                            path=path, content=text, textdata=text)
        fp.close()
    writer.commit()


root = "corpus"
createSearchableData()
