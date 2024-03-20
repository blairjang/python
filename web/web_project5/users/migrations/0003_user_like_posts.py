# Generated by Django 5.0.1 on 2024-02-05 03:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0003_hashtag_post_tags"),
        ("users", "0002_user_profile_image_user_short_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="like_posts",
            field=models.ManyToManyField(
                blank=True,
                related_name="like_users",
                to="posts.post",
                verbose_name="좋아요 누른 post목록",
            ),
        ),
    ]
