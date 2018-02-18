import os
from django.db import models
from django.utils.six import python_2_unicode_compatible

from common.AuthServerModel.models import User
from common.ChatServerModel.models import *


@python_2_unicode_compatible
class TopicFile(models.Model):
    user = models.ForeignKey(
        User,
        related_name="topic_files"
    )
    message = models.ForeignKey(
        TopicMessage,
        related_name="topic_files"
    )
    file = models.FileField()
    created_time = models.DateTimeField('Create Time', auto_now_add=True)

    def get_filename(self):
        filename = os.path.basename(self.file.name)
        print("[[TopicFile]] get_filename")
        print(filename)
        return filename