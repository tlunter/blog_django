from django import forms
from comments.models import Comment
from posts.models import Post
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _

class CommentCreationForm(forms.ModelForm):
    body = forms.CharField(label=_("Body"),
                           help_text=_("The body of the comment"),
                           widget=forms.Textarea)

    post = forms.ModelChoiceField(queryset=Post.objects.all(),
                                  empty_label=None,
                                  label=_("Post"),
                                  help_text=_("The post that the comment is for"),
                                  widget=forms.HiddenInput)

    def clean_post(self):
        try:
            post = Post.objects.get(pk=self.cleaned_data['post'].pk)
        except Post.DoesNotExist:
            raise forms.ValidationError("You cannnot comment on a post that does not exist")

        return post

    def save(self, user, commit=True):
        comment = super(CommentCreationForm, self).save(commit=False) 
        comment.post = self.cleaned_data['post']

        print "Comment: {0}".format(comment.__dict__)

        try:
            comment.created_by
        except User.DoesNotExist:
            comment.created_by = user

        comment.updated_by = user

        if commit:
            comment.save()

        return comment

    class Meta:
        model = Comment
        fields = ('body',)

class CommentDeletionForm(forms.Form):
    verify = forms.BooleanField(label=_("Verify?"),
                                error_messages={ 'required': 'Please check verify' },
                                help_text=_("Verifies you want to delete the comment when checked."),
                                required=True)
