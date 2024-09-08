# Generated by Django 5.1.1 on 2024-09-07 09:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('state', models.IntegerField()),
                ('prev_block_hash', models.CharField(max_length=32)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('bet_percent', models.FloatField()),
                ('start_matter_price', models.FloatField()),
                ('start_idea_price', models.FloatField()),
                ('starts_at', models.DateTimeField(auto_now_add=True)),
                ('ends_at', models.DateTimeField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('block', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='core.block')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('tg_user_id', models.IntegerField()),
                ('matter_ballance', models.FloatField()),
                ('idea_ballance', models.FloatField()),
                ('crypto_wallet_address', models.CharField(blank=True, max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
