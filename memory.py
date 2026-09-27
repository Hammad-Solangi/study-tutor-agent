def build_conversation(messages, limit=10):
    recent_messages = messages[-limit:]

    conversation = []

    for message in recent_messages:
        conversation.append(
            f"{message['role']}: {message['content']}"
        )

    return "\n".join(conversation)
