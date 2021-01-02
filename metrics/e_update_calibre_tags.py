"""
update calibre tags with topics
"""
from pathlib import Path
import os
import xml.etree.ElementTree as ET
import sys
import json
import sqlite3
import process_parameters as pp
sys.path.append('../commons/')
from md5_utils import md5

CONN = sqlite3.connect(pp.CALIBRE_SQLITE_DB)
CUR = CONN.cursor()


def get_book_id(path):
    """gets the book id"""
    CUR.execute('SELECT id FROM books where path = \''+path+'\';')
    for row in CUR:
        book_id = row[0]
        return book_id


def files_list():
    """Lists all PDF files in the calibre library"""
    return list(Path(pp.PDF_FILES_PATH).rglob("*.[pP][dD][fF]"))


for file in files_list():
    paths = str(file).split('/')
    bid = get_book_id(paths[-3]+'/'+paths[-2])

    # getting topics
    tags = set()
    modelMetadata = pp.MODEL_FILE_PATH + '/' + md5(file) + '.metadata'
    with open(modelMetadata) as json_file:
        data = json.load(json_file)
        for topics in data['topics'].split('<hr>'):
            for topic in topics.split('<br>'):
                if topic:
                    tags.add(topic)
            break  # only first topic produces tags
    # print(tags)
    metadataPath = str(file.parents[0])+'/metadata.opf'
    # print(metadataPath)
    if os.path.exists(metadataPath):
        tree = ET.parse(metadataPath)
        root = tree.getroot()
        for elem in root:
            if 'metadata' in elem.tag:
                for subelem in elem:
                    if 'subject' in subelem.tag:
                        if pp.KEEP_EXISTING_TAGS:
                            tags.add(subelem.text.strip())
                        elem.remove(subelem)
                # print(elem.tag)
                for topicTag in tags:
                    newTag = ET.SubElement(elem, 'dc:subject')
                    newTag.text = topicTag

        tree.write(metadataPath)

    updc = 'calibredb set_metadata ' + str(bid) + ' "'+metadataPath+'"'
    # print(updc)
    os.system(updc)
    # break
