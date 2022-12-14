# Generated by Django 4.1 on 2022-09-30 09:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0011_upidetails_bankdetails'),
        ('rentportal', '0013_delete_rent_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rent_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('discriptions', models.TextField(blank=True, max_length=300, null=True)),
                ('sub_mobile', models.CharField(max_length=10)),
                ('mobile', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=200)),
                ('place', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='rent')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='rent')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='rent')),
                ('payment', models.BooleanField(default=False)),
                ('rate', models.IntegerField()),
                ('price_in', models.CharField(choices=[('per_hour', 'per_hour'), ('per_day', 'per_day')], default='per_day', max_length=100)),
                ('available', models.BooleanField(default=False)),
                ('slug', models.SlugField(max_length=255)),
                ('ordernumber', models.CharField(max_length=40)),
                ('booked', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('valid_at', models.DateField(blank=True, null=True)),
                ('item_backed', models.BooleanField(default=False)),
                ('booked_person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rent_booked_person', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.categories')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.city')),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.district')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
