from fastapi import Request

def get_locale(request: Request):
    accept_language = request.headers.get("Accept-Language", "en")
    return accept_language.split(",")[0] if accept_language else "en"
