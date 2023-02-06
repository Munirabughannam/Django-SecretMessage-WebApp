from .models import MessageData


def terminate_link(object_id):
    link = MessageData.objects.get(id=object_id)
    link.delete()
    return True