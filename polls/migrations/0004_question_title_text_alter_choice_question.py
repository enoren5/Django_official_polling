# Generated by Django 4.0.5 on 2022-07-02 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_alter_choice_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='title_text',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.question'),
        ),
    ]
