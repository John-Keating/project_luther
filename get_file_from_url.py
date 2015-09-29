import requests
import urlparse
import os
import pickle

def get_file(url):
    '''
    Takes url and returns a requests.get(url)
    
    Furthermore, create and saves directories/subdirectories and files from a url into your current working directory.
    Thus, you will not have to make more than one request per url.
    However, the function will not check if the file has been updated just if it was downloaded from before.
    '''
    parsed_url = urlparse.urlparse(url)
    path = []
    for item in parsed_url:
        x = item.replace('/','')
        if x != '':
            path.append(x)
    outfile = path[-1]
    path = path[:-1]
    outpath = '/'.join(path)
    
    if not os.path.exists(outpath):
        os.makedirs(outpath)
    if not os.path.isfile(outpath + '/' + outfile):
        r = requests.get(url)
        pickle.dump(r, open('{}'.format(outpath + '/' + outfile), 'wb'))
    else:
        r = pickle.load(open('{}'.format(outpath + '/' + outfile), 'rb'))
    return r