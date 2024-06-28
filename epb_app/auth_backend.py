import pandas as pd # type: ignore
import logging
from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)

class ExcelAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        logger.debug(f"Authenticating user: {username}")

        try:
            df = pd.read_excel(settings.EXCEL_FILE_PATH)
            logger.debug("Excel file loaded successfully")
        except Exception as e:
            logger.error(f"Error reading Excel file: {e}")
            return None

        if username in df['name'].values:
            logger.debug(f"User {username} found in Excel")
            user, created = User.objects.get_or_create(username=username)
            return user
        logger.debug(f"User {username} not found in Excel")
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
           return None