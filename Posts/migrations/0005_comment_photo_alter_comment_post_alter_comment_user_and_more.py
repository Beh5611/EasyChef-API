# Generated by Django 4.1.7 on 2023-03-13 07:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Recipes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Posts', '0004_alter_comment_post_alter_comment_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Posts.post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commented', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Recipes.recipe'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Rating', to='Posts.post'),
        ),
    ]
