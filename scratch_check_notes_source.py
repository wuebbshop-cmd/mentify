import os, sys
sys.path.insert(0, '.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
import django
django.setup()
from prep.models import PrepTopicNotesJob, PrepContentCache

print('Total PrepTopicNotesJob:', PrepTopicNotesJob.objects.count())
print('Complete jobs:', PrepTopicNotesJob.objects.filter(status='complete').count())
print('Pending jobs:', PrepTopicNotesJob.objects.filter(status='pending').count())
print('Failed jobs:', PrepTopicNotesJob.objects.filter(status='failed').count())
