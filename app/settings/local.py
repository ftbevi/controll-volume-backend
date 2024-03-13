from .base import *  # noqa: F403, F401

# Static files (CSS, JavaScript, Images)
DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

STATIC_ROOT = os.path.join(
    os.path.join(os.path.join(PROJECT_FOLDER, "resources", "static"))
)
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(os.path.join(os.path.join(PROJECT_FOLDER, "resources", "media")))
MEDIA_URL = "/media/"
