from django.core.exceptions import ValidationError

def validate_file_size(value):
    filesize= value.size
    
    if filesize > 8485760:
        raise ValidationError("You cannot upload file more than 8MB")
    else:
        return value


def validate_picture_size(value):
    filesize= value.size
    
    if filesize > 4485760:
        raise ValidationError("You cannot upload file more than 4MB")
    else:
        return value