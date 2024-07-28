from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import QuickTips


@registry.register_document
class QuickTipsDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'quicktips'
        # Settings for the index
        settings = {
          "number_of_shards": 1,
          "number_of_replicas": 0
        }

    class Django:
        model = QuickTips  # The model associated with this Document

        # The fields to index in Elasticsearch
        fields = [
            'title',
            'content',
            'posted_at',
        ]