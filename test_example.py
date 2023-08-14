# content of test_sample.py
def inc(x):
    return x + 1


def test_answer():
    assert inc(4) == 5


def read_txt(target_url):
    import urllib.request
    data = urllib.request.urlopen(target_url)
    no = 0
    for line in data: # files are iterable
        no += 1
    return no

def test_lineno():
    assert read_txt("https://www.w3.org/TR/2003/REC-PNG-20031110/iso_8859-1.txt") > 5


def get_gdal():
    from osgeo import gdal
    return(gdal.__version__)

def test_gdal():
    assert not (get_gdal() == "")
