# Generated by Django 4.1.3 on 2022-11-20 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Biography',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default='my.mail@gmail.com', max_length=100)),
                ('website', models.CharField(default='', max_length=70)),
                ('socialProfile', models.CharField(default='', max_length=70)),
            ],
            options={
                'db_table': 'Biography',
            },
        ),
        
        
        migrations.RemoveField(
            model_name='portfolio',
            name='Biography',
        ),
        migrations.AlterModelTable(
            name='references',
            table='References',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='biography',
            field=models.ForeignKey(default='', max_length=70, on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.biography'),
        ),
    ]
