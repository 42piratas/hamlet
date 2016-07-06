import nltk
import hg


def hfind_entities():
    for w in hg.content_raw_words:
        nameEnt = nltk.ne_chunk(hg.content_raw_words)

        namedEnt.draw()


if __name__ == '__main__':
    from hextractor import hextract
    from hfilter import hfilter
    hextract()
    hfilter()
    hfind_entities()
