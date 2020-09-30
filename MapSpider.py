import urllib3.request
from bs4 import BeautifulSoup
from datetime import date

date = date.today()
day=date.strftime("%d")
month=date.strftime("%b")
year=date.strftime("%Y")
WILAYAH_VALUES = ['aceh', 'sumut', 'sumbar', 'riau', 'kepri', 'jambi', 'bengkulu', 'sumsel', 'babel', 'lampung', 'banten', 'dkijakarta', 'jabar', 'jateng', 'jatim', 'yogya', 'bali', 'ntb', 'ntt', 'kalbar', 'kalsel', 'kalteng', 'kaltim', 'kaltara', 'gorontalo', 'sulbar', 'sulsel', 'sultra', 'sulteng', 'sulut', 'maluku', 'malut', 'pabar', 'papua', 'asean', 'indonesia', 'sumatera', 'kalimantan']
http = urllib3.PoolManager()

for val in WILAYAH_VALUES:
    url = "https://www.bmkg.go.id/cuaca/kebakaran-hutan.bmkg?index=dc&wil="+val+"&day=obs"
    html = http.request('GET', url)
    soup = BeautifulSoup(html.data, features="lxml")
    imgs = soup.find("img", {"class":"featurette-image img-responsive"})
    link = imgs['src']
    filename = imgs['title'].split('-')[1].split('(')[0].strip().replace(" ","_")
    
    imagefile = open(filename + '_Obs_DC_' + day + month + year + ".jpg", 'wb')
    imagefile.write(http.request('GET', link).data)
    imagefile.close()
