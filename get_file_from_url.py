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
    
    Also, if the url is bad then it will print an Error and will return None
    '''
    parsed_url = urlparse.urlparse(url)
    path = []
    for item in parsed_url:
        for x in item.split("/"):
            if x != '':
                path.append(x)
    outfile = path[-1]
    path = path[:-1]
    outpath = '/'.join(path)
    
    if not os.path.exists(outpath):
        os.makedirs(outpath)
    if not os.path.isfile(outpath + '/' + outfile):
        r = requests.get(url)
        if r.status_code != requests.codes.ok:
            print 'Error: request.get(url) Status NOT 200'
            return None 
        pickle.dump(r, open('{}'.format(outpath + '/' + outfile + '.p'), 'wb'))
    else:
        r = pickle.load(open('{}'.format(outpath + '/' + outfile + '.p'), 'rb'))
    return r