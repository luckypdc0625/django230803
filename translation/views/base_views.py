from django.shortcuts import render, get_object_or_404
from .. import tl

def index(request):
    source_sentence = str(request.GET.get('kw', '내용을 입력해주세요.'))
    dest_sentence = tl.main(source_sentence, "ko", "ja")
    context = {'dest_sentence' : dest_sentence}
    return render(request, 'translation/translation_main.html', context)