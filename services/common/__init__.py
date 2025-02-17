from .models import db, migrate  # ✅ models.py에서 db와 migrate 가져오기

__all__ = ["db", "migrate"]