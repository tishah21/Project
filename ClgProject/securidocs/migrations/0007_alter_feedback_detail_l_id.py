# Generated by Django 4.0.1 on 2022-03-20 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('securidocs', '0006_alter_feedback_detail_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback_detail',
            name='l_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='securidocs.login'),
        ),
    ]