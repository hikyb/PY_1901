import xadmin
from .models import Ads, Catrgory, Tag, Article

xadmin.site.register(Ads)
xadmin.site.register(Catrgory)
xadmin.site.register(Tag)


class ArticleAdmin:
    # 模型字段想要使用ueditor样式必须注册模型管理类
    style_fields = {'body': 'ueditor'}


xadmin.site.register(Article, ArticleAdmin)

