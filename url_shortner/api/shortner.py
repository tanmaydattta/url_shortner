import uuid
from .models import urlShortener

def generate_random_string(string_length=6):
    """
    Returns a random string of length string_length.
    This will be appended to the shortened link and stored in db
    a url.
    """
    # Convert UUID format to a Python string.
    random = str(uuid.uuid4())

    # Remove the UUID '-'.
    random = random.replace("-", "")

    # Return the random string.
    return random[0:string_length]


def create_url(url_to_be_shortened):
    """
    Check if a string is already in use on the redis server and create a new
    one if needed.
    Create the shortened URL and save it on Redis
    """
    strng = generate_random_string()

    if urlShortener.objects.all().filter(shorturl=strng).count()>0:
        create_url(url_to_be_shortened)

    else:
        return strng