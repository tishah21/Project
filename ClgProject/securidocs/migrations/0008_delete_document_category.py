# Generated by Django 4.0.1 on 2022-03-20 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('securidocs', '0007_alter_feedback_detail_l_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='document_category',
        ),
    ]