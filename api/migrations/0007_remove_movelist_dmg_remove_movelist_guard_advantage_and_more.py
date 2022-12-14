# Generated by Django 4.1.1 on 2022-09-08 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_rename_special_props_movelist_comment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movelist',
            name='dmg',
        ),
        migrations.RemoveField(
            model_name='movelist',
            name='guard_advantage',
        ),
        migrations.RemoveField(
            model_name='movelist',
            name='move_name',
        ),
        migrations.AddField(
            model_name='movelist',
            name='damage',
            field=models.IntegerField(null=True, verbose_name='damage'),
        ),
        migrations.AddField(
            model_name='movelist',
            name='guard_adv',
            field=models.IntegerField(null=True, verbose_name='guard advantage'),
        ),
        migrations.AddField(
            model_name='movelist',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='movelist',
            name='move',
            field=models.CharField(max_length=200, null=True, verbose_name='move'),
        ),
        migrations.AlterField(
            model_name='movelist',
            name='comment',
            field=models.CharField(blank=True, max_length=500, verbose_name='comment'),
        ),
        migrations.AlterField(
            model_name='movelist',
            name='startup',
            field=models.IntegerField(verbose_name='startup'),
        ),
        migrations.AlterField(
            model_name='movelist',
            name='stun',
            field=models.IntegerField(verbose_name='stun'),
        ),
    ]
