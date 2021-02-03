from django.http import HttpResponse

class StripeWH_Handler:
    ''' handle stripe webhooks'''
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        ''' handle generic/unexpected webhook event'''
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        ''' handle payment intent.succeeded web hook from
        stripe
        '''
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_failed(self, event):
        ''' handle payment intent.succeeded web hook from
        stripe
        '''
        return HttpResponse(
            content=f'you got no money! Webhook received: {event["type"]}',
            status=200)
