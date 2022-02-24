from rest_framework import routers
from office.views.department_view import DepartmentViewSet
from office.views.designation_view import DesignationViewSet
from office.views.bank_view import BankViewSet
from office.views.payment_view import PaymentViewSet

router = routers.DefaultRouter()

router.register('department', DepartmentViewSet)
router.register('designation', DesignationViewSet)
router.register('bank', BankViewSet)
router.register('payment', PaymentViewSet)

urlpatterns = [] + router.urls
