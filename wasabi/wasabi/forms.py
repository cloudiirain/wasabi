from django.forms import ModelForm
from directory.models import Chapter

class ChapterForm(ModelForm):
    class Meta:
        model = Chapter
        fields = ['title', 'series', 'owner', 'order', 'body']