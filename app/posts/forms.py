from django import forms
from posts.models import Post
from django.utils.translation import ugettext, ugettext_lazy as _

class PostCreationForm(forms.ModelForm):

    subject = forms.CharField(label=_("Subject"),
                              help_text=_("The subject of the new post"))
    body = forms.CharField(label=_("Body"),
                           help_text=_("The body of the given text"),
                           widget=forms.Textarea)
    visible = forms.BooleanField(label=_("Visible?"),
                                 help_text=_("Whether or not the post is visible"),
                                 required=False)

    def save(self, user, commit=True):
        post = super(PostCreationForm, self).save(commit=False) 
        if not post.created_by:
            post.created_by = user
        post.updated_by = user

        if commit:
            post.save()

        return post

    class Meta:
        model = Post
        fields = ("subject","body","visible",)

class PostDeletionForm(forms.Form):
    verify = forms.BooleanField(label=_("Verify?"),
                                error_messages={ 'required': 'Please check verify' },
                                help_text=_("Verifies you want to delete the post when checked."),
                                required=True)
