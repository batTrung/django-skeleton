from .base import *


# ==============================================================================
# CORE SETTINGS
# ==============================================================================


# ==============================================================================
# SECURITY SETTINGS
# ==============================================================================

CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
SECURE_HSTS_SECONDS = 60 * 60 * 24 * 7 * 52  # one year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_SSL_REDIRECT = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True


# ==============================================================================
# LOGGING SETTINGS
# ==============================================================================


# ==============================================================================
# CACHE SETTINGS
# ==============================================================================

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(os.path.dirname(BASE_DIR), 'apps/cache'),
    }
}


# ==============================================================================
# THIRD-PARTY APPS SETTINGS
# ==============================================================================
