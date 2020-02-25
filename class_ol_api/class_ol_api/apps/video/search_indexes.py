from haystack import indexes
from .models import Video


class VideoIndex(indexes.SearchIndex, indexes.Indexable):
    """视频索引数据模型类"""
    text = indexes.CharField(document=True, use_template=True)
    id = indexes.IntegerField(model_attr='id')
    title = indexes.CharField(model_attr='name')
    focus_content = indexes.CharField(model_attr='focus_content')
    video_img = indexes.CharField(model_attr='video_img')

    def get_model(self):
        """返回建立索引的模型类"""
        return Video

    def index_queryset(self, using=None):
        """返回要建立索引的数据查询集"""
        return self.get_model().objects.filter(video_status=1, is_show=True)
