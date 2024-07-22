from .chat import chat_session

def chat_bot(request):
    if request.method == "POST":
        content = request.POST['content']
        
        message = BotMessage(
            user=request.user,
            sender=BotMessage.USER,
            content=content,
        )
        message.save()

        response = chat_session.send_message(content)
        response = response.text

        replay = BotMessage(
            user=request.user,
            sender=BotMessage.BOT,
            content=response,
        )
        replay.save()
    message_list = BotMessage.objects.filter(user=request.user).order_by("date")

    return render(request, "chat_bot.html", { 'message_list': message_list })