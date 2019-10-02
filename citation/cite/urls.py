from rest_framework import routers
from .api import JournalCiteViewset


router = routers.DefaultRouter()
router.register('api/cite', JournalCiteViewset, 'journal')
urlpatterns = router.urls
