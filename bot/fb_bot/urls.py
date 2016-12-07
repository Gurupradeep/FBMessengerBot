from django.conf.urls import include,url
from .views import fb_botView
urlpatterns = [

	### derine a random string as end point urk( otheres shouldn't know this)
	url(r'^66d2b8f4a09cd35cb23076a1da5d51529136a3373fd570b122/?$',fb_botView.as_view())
]