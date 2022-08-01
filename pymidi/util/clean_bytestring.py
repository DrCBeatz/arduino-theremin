def clean_bytestring(bstr: bytes) -> str:
    '''
    removes non-numeric characters (except for 'p' and 'v') from
    bytestring (by first converting python bytestring to unicode
    string) using regular expressions and returns string.
    '''
    import re
    if bstr == None:
        return 0
    result = bstr.decode('utf-8')
    return re.sub("[^vp0-9]", "", result)