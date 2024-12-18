# Generated by Django 5.1.2 on 2024-11-12 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stud_name', models.CharField(max_length=100)),
                ('stud_age', models.IntegerField()),
                ('stud_sch', models.CharField(max_length=100)),
                ('stud_des', models.TextField()),
                ('stud_pass', models.ImageField(upload_to='')),
                ('stud_reg', models.IntegerField()),
            ],
        ),
    ]
