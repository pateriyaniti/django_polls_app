from rest_framework import routers

from .api_views import ChoiceViewSet, QuestionViewSet

router = routers.DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'Choice', ChoiceViewSet)

urlpatterns = router.urls