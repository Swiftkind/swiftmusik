# Generated by Django 2.0.1 on 2018-02-02 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0003_vote'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaylistLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('play', 'Play'), ('pause', 'Pause'), ('stop', 'Stop')], default='play', max_length=15)),
                ('timestamp', models.TimeField(auto_now_add=True)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player.Video')),
            ],
        ),
        migrations.AlterField(
            model_name='vote',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='player.Video'),
        ),
    ]