# Generated by Django 2.2.5 on 2020-01-20 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cultures', '0003_auto_20200120_0627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensor',
            name='culture',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='noeudCollecteur',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='valueType',
        ),
        migrations.RemoveField(
            model_name='actuatorhistory',
            name='Actuator',
        ),
        migrations.RemoveField(
            model_name='data',
            name='sensor',
        ),
        migrations.RemoveField(
            model_name='scheduledactuators',
            name='actuator',
        ),
        migrations.AddField(
            model_name='actuatorhistory',
            name='action',
            field=models.TextField(default='up'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='actuatorhistory',
            name='noeudCollecteur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='actuatorHistory', to='Cultures.NoeudCollecteur'),
        ),
        migrations.AddField(
            model_name='data',
            name='noeudCollecteur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Cultures.NoeudCollecteur'),
        ),
        migrations.AddField(
            model_name='noeudcollecteur',
            name='culture',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='noeudCollecteurs', to='Cultures.Culture'),
        ),
        migrations.AddField(
            model_name='noeudcollecteur',
            name='parameters',
            field=models.ManyToManyField(to='Cultures.CultureParameters'),
        ),
        migrations.AddField(
            model_name='noeudcollecteur',
            name='status',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scheduledactuators',
            name='action',
            field=models.TextField(default='up'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scheduledactuators',
            name='noeudCollecteur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='actuatorSchedule', to='Cultures.NoeudCollecteur'),
        ),
        migrations.DeleteModel(
            name='Actuator',
        ),
        migrations.DeleteModel(
            name='Sensor',
        ),
    ]
