import uuid


def unique_order_id_generator(instance):
    new_order_id = uuid.uuid4().hex[:5].upper()
    klass = instance.__class__
    qs_exist = klass.objects.filter(order_id=new_order_id).exists()
    if qs_exist:
        return unique_order_id_generator(instance)
    return new_order_id
