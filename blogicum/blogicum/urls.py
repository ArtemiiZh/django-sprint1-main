from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Подключаем ВСЕ пути блога один раз. Django сам найдёт внутри и posts/, и category/
    path('', include('blog.urls')),
    
    # Подключаем пути страниц about и rules
    path('pages/', include('pages.urls')),
    
    # Админка
    path('admin/', admin.site.urls),
]
