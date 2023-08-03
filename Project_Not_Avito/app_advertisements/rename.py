from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('app_adverisements', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel("app_advertisements_advertisement", "advertisement")
    ]