from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import CommentModel


@receiver(post_save, sender=CommentModel)
def notify_new_comment(sender, instance, created, **kwargs):
    print("Got here")
    if created:
        email = [instance.post.user_id.email]

        send_mail(
            subject=f"There is a new comment on your post '{instance.post.title}'",
            message=f"{instance.user_id.username} commented on '{instance.post.title}'",
            from_email='test@google.com',
            recipient_list=email
        )

@receiver(post_save, sender=CommentModel)
def notify_comment_accepted(sender, instance, created, **kwargs):
    if instance.is_confirmed is True and not created:
        email = [instance.user_id.email]

        send_mail(
            subject=f"Your comment was accepted by '{instance.post.user_id.username}'",
            message=f"'{instance.post.user_id.username}' accepted your comment.",
            from_email='test@google.com',
            recipient_list=email
        )
