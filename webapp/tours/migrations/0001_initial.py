# Generated by Django 3.0.1 on 2019-12-20 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purpose', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('mode_of_travel', models.CharField(max_length=50)),
                ('ticket_cost', models.CharField(max_length=10)),
                ('origin_cab_fare', models.CharField(max_length=10)),
                ('destination_cab_fare', models.CharField(max_length=10)),
                ('hotel_cost', models.CharField(max_length=10)),
                ('hotel_receipt', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('conveyance', models.CharField(max_length=255)),
                ('additional_information', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField()),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('Submitted', 'Submitted'), ('Submitted to Finance', 'Submitted to Finance'), ('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Request for Information', 'Request for Information')], default='draft', max_length=25)),
                ('feedback_date', models.DateTimeField(null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('approving_manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='approved_tours', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_tours', to=settings.AUTH_USER_MODEL)),
                ('financial_manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='financially_approved_tours', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
