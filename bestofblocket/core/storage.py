from django.contrib.staticfiles.storage import CachedFilesMixin

from pipeline.storage import PipelineMixin

from storages.backends.s3boto import S3BotoStorage


class S3PipelineCachedStorage(PipelineMixin, CachedFilesMixin, S3BotoStorage):
    pass