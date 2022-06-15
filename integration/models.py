from django.db import models

# Create your models here.


class Team(models.Model):
    TEAM_TYPES = [("slack", "Slack"),
                   ("discord", "Discord")]
    name = models.CharField(max_length=200)
    team_id = models.CharField(max_length=20)
    bot_user_id = models.CharField(max_length=20)
    bot_access_token = models.CharField(max_length=100)
    chat_type = models.CharField(max_length=25, choices=TEAM_TYPES)

    def __str__(self):
        return f"{self.chat_type}-{self.team_id}: {self.name}"
