from rest_framework.pagination import PageNumberPagination


class CourseListPageNumberPagintation(PageNumberPagination):
    page_size = 10  # 每一页显示的数量，没有设置页码，则不进行分页
    page_query_param = 'page'  # 地址上代表页码的变量名, 默认为page
    # 允许客户端通过指定的参数名来设置每一页数据量的大小，默认是size
    page_size_query_param = 'size'
    max_page_size = 20  # 限制每一页最大展示的数据量


class CourseAllPageNumberPagination(PageNumberPagination):
    page_size = 6  # 每一页显示的数量，没有设置页码，则不进行分页
    page_query_param = 'page'  # 地址上代表页码的变量名, 默认为page
    # 允许客户端通过指定的参数名来设置每一页数据量的大小，默认是size
    page_size_query_param = 'size'
    max_page_size = 20  # 限制每一页最大展示的数据量


class RankingPageNumberPagination(PageNumberPagination):
    page_size = 8  # 每一页显示的数量，没有设置页码，则不进行分页
    page_query_param = 'page'  # 地址上代表页码的变量名, 默认为page
    # 允许客户端通过指定的参数名来设置每一页数据量的大小，默认是size
    page_size_query_param = 'size'
    max_page_size = 20  # 限制每一页最大展示的数据量