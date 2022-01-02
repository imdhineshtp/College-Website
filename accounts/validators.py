from django.core.exceptions import ValidationError

def validProfile(value):
    filesize = value.size

    if filesize>2097157:
        raise ValidationError("The maximum file size that can be uploaded in 2MB")
    else:
        return value

def validSign(value):
    filesize = value.size
    
    if filesize>102400:
        raise ValidationError("The maximum file size that can be uploaded in 100KB")
    else:
        return value