from rest_framework import serializers
from .models import EmailLog


class EmailLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailLog
        fields = ['id','to_email','subject','message_body','created_at','sent_by','lead','client']


class EmailSendSerializer(serializers.Serializer):
    to = serializers.EmailField(label='To')
    subject = serializers.CharField(max_length=255, label='Subject')
    message = serializers.CharField(style={'base_template': 'textarea.html'}, label="Message")


    def validate_attachments(self, files):
        if len(files) > 5:
            raise serializers.ValidationError('You cannot add more than 5 files')

        for file in files:
            if file.size > 10 * 1024 * 1024:  # 10 MB
                raise serializers.ValidationError(f"File: {file.name} is too big!")

        return files