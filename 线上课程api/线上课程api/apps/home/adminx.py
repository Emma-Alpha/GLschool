import xadmin
from xadmin import views


class BaseSetting(object):
    """xadmin的基本配置"""
    enable_themes = True  # 开启主题切换功能
    use_bootswatch = True


xadmin.site.register(views.BaseAdminView, BaseSetting)


class GlobalSettings(object):
    """xadmin的全局配置"""
    site_title = "广理工学院后台管理"  # 设置站点标题
    site_footer = "广东理工学院"  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠


xadmin.site.register(views.CommAdminView, GlobalSettings)

# 轮播图
from .models import Banner, Timer


class BannerXAdmin(object):
    list_display = ["title", "orders", "is_show"]


class TimerXAdmin(object):
    list_display = ['title', 'orders', 'is_show']


xadmin.site.register(Banner, BannerXAdmin)
xadmin.site.register(Timer,TimerXAdmin)
