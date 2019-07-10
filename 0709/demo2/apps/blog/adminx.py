import xadmin
from .models import Ads, Catrgory, Tag, Article

xadmin.site.register(Ads)
xadmin.site.register(Catrgory)
xadmin.site.register(Tag)
xadmin.site.register(Article)
