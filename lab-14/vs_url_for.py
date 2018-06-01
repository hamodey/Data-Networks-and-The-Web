from flask import url_for

<<<<<<< HEAD
URL_PREFIX = '/usr/253'
=======
URL_PREFIX = '/usr/168'
>>>>>>> d26b24f1f403b657837d68de4d28ee48e746323b

def vs_url_for(view):
    url = url_for(view)
    url = URL_PREFIX + url
    return url


