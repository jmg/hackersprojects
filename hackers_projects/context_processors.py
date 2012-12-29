def processor(request):

    return {'profile': request.session.get("user") }

